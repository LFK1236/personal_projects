using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using GameDatabase.Models;

namespace GameDatabase.Data
{
    public class GameDatabaseContext : DbContext
    {
        public GameDatabaseContext (DbContextOptions<GameDatabaseContext> options)
            : base(options)
        {
        }

        public DbSet<GameDatabase.Models.Game> Game { get; set; } = default!;
    }
}
