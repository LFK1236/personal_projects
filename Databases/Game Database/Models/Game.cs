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
        public string? ReleaseYear { get; set; } = string.Empty;

        public int Rating { get; set; }

        public string? Genre { get; set; } = string.Empty;
        public string? Developer { get; set; } = string.Empty;
        public string? Publisher { get; set; } = string.Empty;
    }
}