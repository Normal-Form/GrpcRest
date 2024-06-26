using Microsoft.AspNetCore.Mvc;
using GrpcRest.Common.Models;

namespace RestController.Controllers;

[ApiController]
[Route("[controller]")]
public class StudentsController : ControllerBase
{
    private readonly ILogger<StudentsController> _logger;

    public StudentsController(ILogger<StudentsController> logger)
    {
        _logger = logger;
    }

    [HttpGet(Name = "StudentData")]
    public StudentList Get()
    {
        return Helper.SampleData();
    }
}
