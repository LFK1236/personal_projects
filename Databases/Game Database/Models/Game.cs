using System.ComponentModel.DataAnnotations;

namespace Game_Database.Models
{
    public class Game
    {
        [Required]
        public string? Title { get; set; }
        [Required]
        public string? Release { get; set; }
    }
}