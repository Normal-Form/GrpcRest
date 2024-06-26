from locust import User, task, HttpUser, FastHttpUser
from locust.exception import LocustError

import time
from typing import Any, Callable

import grpc
from grpc_interceptor import ClientInterceptor

import student_pb2
import student_pb2_grpc

class LocustInterceptor(ClientInterceptor):
    def __init__(self, environment, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.env = environment

    def intercept(
        self,
        method: Callable,
        request_or_iterator: Any,
        call_details: grpc.ClientCallDetails,
    ):
        response = None
        exception = None
        start_perf_counter = time.perf_counter()
        response_length = 0
        try:
            response = method(request_or_iterator, call_details)
            response_length = response.result().ByteSize()
        except grpc.RpcError as e:
            exception = e

        self.env.events.request.fire(
            request_type="grpc",
            name=call_details.method,
            response_time=(time.perf_counter() - start_perf_counter) * 1000,
            response_length=response_length,
            response=response,
            context=None,
            exception=exception,
        )
        return response


class GrpcUser(User):
    abstract = True
    stub_class = None

    def __init__(self, environment):
        super().__init__(environment)
        for attr_value, attr_name in ((self.host, "host"), (self.stub_class, "stub_class")):
            if attr_value is None:
                raise LocustError(f"You must specify the {attr_name}.")

        self._channel = grpc.insecure_channel(self.host)
        interceptor = LocustInterceptor(environment=environment)
        self._channel = grpc.intercept_channel(self._channel, interceptor)

        self.stub = self.stub_class(self._channel)


class StudentGrpcGzipUser(GrpcUser):
    host = "localhost:5093"
    stub_class = student_pb2_grpc.StudentDataStub

    @task
    def getList(self):
        self.stub.GetList(student_pb2.GetRequest(), compression=grpc.Compression.Gzip)


class StudentGrpcUser(GrpcUser):
    host = "localhost:5093"
    stub_class = student_pb2_grpc.StudentDataStub

    @task
    def getList(self):
        self.stub.GetList(student_pb2.GetRequest())

class StudentRestFastUser(FastHttpUser):
    host = "http://localhost:5172"
    @task
    def studentdata(self):
        self.client.get("/students")

class StudentRestUser(HttpUser):
    host = "http://localhost:5172"
    @task
    def studentdata(self):
        self.client.get("/students")
