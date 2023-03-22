using System.ComponentModel.DataAnnotations;

namespace GameDatabase.Models
{
    public class Genre
    {
        public Genre(string genreName)
        {
            GenreName = genreName;
        }

        [Display(Name = "Genre")]
        [Required]
        public string GenreName { get; set; }
    }
}
