namespace GrpcRest.Common.Models;

public class Student
{
    public int Id { get; set; }
    public string FirstName { get; set; }
    public string LastName { get; set; }
    public int Age { get; set; }
    public string Gender { get; set; }
    public ContactInfo ContactInfo { get; set; }
    public Address Address { get; set; }
    public AcademicInfo AcademicInfo { get; set; }
    public List<ExtracurricularActivity> ExtracurricularActivities { get; set; }
}
