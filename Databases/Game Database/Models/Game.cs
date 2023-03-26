using System.ComponentModel.DataAnnotations;

namespace GameDatabase.Models
{
    public class Game
    {
        public int Id { get; set; }

        [Required]
        public string Title { get; set; } = string.Empty;

        [Display(Name = "Release Year")]
        [Required]
        public int ReleaseYear { get; set; }

        public int Rating { get; set; } = 0;

        public string Genre { get; set; } = string.Empty;

        public string Developer { get; set; } = string.Empty;

        public string Publisher { get; set; } = string.Empty;

        public string Platform { get; set; } = string.Empty;

        public Game(string title, int releaseYear)
        {
            Title = title;
            ReleaseYear = releaseYear;
        }
    }
}