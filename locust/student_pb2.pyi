from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetReply(_message.Message):
    __slots__ = ("StudentList",)
    STUDENTLIST_FIELD_NUMBER: _ClassVar[int]
    StudentList: StudentList
    def __init__(self, StudentList: _Optional[_Union[StudentList, _Mapping]] = ...) -> None: ...

class ContactInfo(_message.Message):
    __slots__ = ("email", "phone")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    email: str
    phone: str
    def __init__(self, email: _Optional[str] = ..., phone: _Optional[str] = ...) -> None: ...

class Address(_message.Message):
    __slots__ = ("street", "city", "state", "zip")
    STREET_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ZIP_FIELD_NUMBER: _ClassVar[int]
    street: str
    city: str
    state: str
    zip: str
    def __init__(self, street: _Optional[str] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., zip: _Optional[str] = ...) -> None: ...

class Course(_message.Message):
    __slots__ = ("courseId", "courseName", "grade")
    COURSEID_FIELD_NUMBER: _ClassVar[int]
    COURSENAME_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    courseId: str
    courseName: str
    grade: str
    def __init__(self, courseId: _Optional[str] = ..., courseName: _Optional[str] = ..., grade: _Optional[str] = ...) -> None: ...

class AcademicInfo(_message.Message):
    __slots__ = ("major", "year", "gpa", "courses")
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    GPA_FIELD_NUMBER: _ClassVar[int]
    COURSES_FIELD_NUMBER: _ClassVar[int]
    major: str
    year: str
    gpa: float
    courses: _containers.RepeatedCompositeFieldContainer[Course]
    def __init__(self, major: _Optional[str] = ..., year: _Optional[str] = ..., gpa: _Optional[float] = ..., courses: _Optional[_Iterable[_Union[Course, _Mapping]]] = ...) -> None: ...

class ExtracurricularActivity(_message.Message):
    __slots__ = ("activityId", "activityName", "role")
    ACTIVITYID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYNAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    activityId: int
    activityName: str
    role: str
    def __init__(self, activityId: _Optional[int] = ..., activityName: _Optional[str] = ..., role: _Optional[str] = ...) -> None: ...

class Student(_message.Message):
    __slots__ = ("id", "firstName", "lastName", "age", "gender", "contactInfo", "address", "academicInfo", "extracurricularActivities")
    ID_FIELD_NUMBER: _ClassVar[int]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    CONTACTINFO_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ACADEMICINFO_FIELD_NUMBER: _ClassVar[int]
    EXTRACURRICULARACTIVITIES_FIELD_NUMBER: _ClassVar[int]
    id: int
    firstName: str
    lastName: str
    age: int
    gender: str
    contactInfo: ContactInfo
    address: Address
    academicInfo: AcademicInfo
    extracurricularActivities: _containers.RepeatedCompositeFieldContainer[ExtracurricularActivity]
    def __init__(self, id: _Optional[int] = ..., firstName: _Optional[str] = ..., lastName: _Optional[str] = ..., age: _Optional[int] = ..., gender: _Optional[str] = ..., contactInfo: _Optional[_Union[ContactInfo, _Mapping]] = ..., address: _Optional[_Union[Address, _Mapping]] = ..., academicInfo: _Optional[_Union[AcademicInfo, _Mapping]] = ..., extracurricularActivities: _Optional[_Iterable[_Union[ExtracurricularActivity, _Mapping]]] = ...) -> None: ...

class StudentList(_message.Message):
    __slots__ = ("students",)
    STUDENTS_FIELD_NUMBER: _ClassVar[int]
    students: _containers.RepeatedCompositeFieldContainer[Student]
    def __init__(self, students: _Optional[_Iterable[_Union[Student, _Mapping]]] = ...) -> None: ...
