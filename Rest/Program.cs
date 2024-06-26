using GrpcRest.Common.Models;

var builder = WebApplication.CreateBuilder(args);

// NOTE: uncomment to enable compression
// builder.Services.AddResponseCompression(options =>
// {
//     options.EnableForHttps = true;
// });

var app = builder.Build();

// NOTE: uncomment to enable compression
// app.UseResponseCompression();

app.MapGet("/students", () => Helper.SampleData());
// NOTE: adding task and async to see if it impacts perf.
app.MapGet("/taskstudents", () => Task.FromResult(Helper.SampleData()));
app.MapGet("/asyncstudents", async () => await Task.FromResult(Helper.SampleData()));

app.Run();
