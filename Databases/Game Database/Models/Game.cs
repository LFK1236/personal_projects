using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Configuration;
using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.ComponentModel.DataAnnotations;

namespace Game_Database.Models
{
    public class Game
    {
        [Required]
        public string? Title { get; set; }
        [Required]
        public string? Release_year { get; set; }

        public int Rating { get; set; }
    }
}