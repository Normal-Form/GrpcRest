namespace GrpcRest.Common.Models;

public class AcademicInfo
{
    public string Major { get; set; }
    public string Year { get; set; }
    public double GPA { get; set; }
    public List<Course> Courses { get; set; }
}
