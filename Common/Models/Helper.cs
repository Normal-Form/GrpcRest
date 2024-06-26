namespace GrpcRest.Common.Models;

public class Helper
{
    public static StudentList SampleData()
    {
        return new StudentList
        {
            Students = new List<Student>
            {
                new Student
                {
                    Id = 1,
                    FirstName = "John",
                    LastName = "Doe",
                    Age = 20,
                    Gender = "Male",
                    ContactInfo = new ContactInfo
                    {
                        Email = "john.doe@example.com",
                        Phone = "555-1234"
                    },
                    Address = new Address
                    {
                        Street = "123 Main St",
                        City = "Anytown",
                        State = "CA",
                        Zip = "12345"
                    },
                    AcademicInfo = new AcademicInfo
                    {
                        Major = "Computer Science",
                        Year = "Sophomore",
                        GPA = 3.8,
                        Courses = new List<Course>
                        {
                            new Course
                            {
                                CourseId = "CS101",
                                CourseName = "Introduction to Computer Science",
                                Grade = "A"
                            },
                            new Course
                            {
                                CourseId = "MATH101",
                                CourseName = "Calculus I",
                                Grade = "B+"
                            }
                        }
                    },
                    ExtracurricularActivities = new List<ExtracurricularActivity>
                    {
                        new ExtracurricularActivity
                        {
                            ActivityId = 1,
                            ActivityName = "Soccer",
                            Role = "Player"
                        },
                        new ExtracurricularActivity
                        {
                            ActivityId = 2,
                            ActivityName = "Chess Club",
                            Role = "Member"
                        }
                    }
                },
                new Student
                {
                    Id = 2,
                    FirstName = "Jane",
                    LastName = "Smith",
                    Age = 22,
                    Gender = "Female",
                    ContactInfo = new ContactInfo
                    {
                        Email = "jane.smith@example.com",
                        Phone = "555-5678"
                    },
                    Address = new Address
                    {
                        Street = "456 Elm St",
                        City = "Othertown",
                        State = "NY",
                        Zip = "67890"
                    },
                    AcademicInfo = new AcademicInfo
                    {
                        Major = "Biology",
                        Year = "Senior",
                        GPA = 3.9,
                        Courses = new List<Course>
                        {
                            new Course
                            {
                                CourseId = "BIO201",
                                CourseName = "Genetics",
                                Grade = "A"
                            },
                            new Course
                            {
                                CourseId = "CHEM201",
                                CourseName = "Organic Chemistry",
                                Grade = "A-"
                            }
                        }
                    },
                    ExtracurricularActivities = new List<ExtracurricularActivity>
                    {
                        new ExtracurricularActivity
                        {
                            ActivityId = 3,
                            ActivityName = "Debate Team",
                            Role = "Captain"
                        },
                        new ExtracurricularActivity
                        {
                            ActivityId = 4,
                            ActivityName = "Volunteer Club",
                            Role = "Coordinator"
                        }
                    }
                }
            }
        };
    }    
}
