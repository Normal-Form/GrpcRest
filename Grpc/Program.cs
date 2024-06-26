// NOTE: uncomment to enable compression
// using System.IO.Compression;
using Grpc.Services;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddGrpc((opt) => {
// NOTE: uncomment to enable compression
//     opt.ResponseCompressionAlgorithm = "gzip";
//     opt.ResponseCompressionLevel = CompressionLevel.SmallestSize;
});

var app = builder.Build();

// Configure the HTTP request pipeline.
app.MapGrpcService<GreeterService>();
app.MapGrpcService<StudentService>();
app.MapGet("/", () => "Communication with gRPC endpoints must be made through a gRPC client. To learn how to create a client, visit: https://go.microsoft.com/fwlink/?linkid=2086909");

app.Run();
