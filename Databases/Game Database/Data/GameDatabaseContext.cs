using GameDatabase.Models;
using Microsoft.EntityFrameworkCore;

namespace GameDatabase.Data
{
    public class GameDatabaseContext : DbContext
    {
        public GameDatabaseContext(DbContextOptions<GameDatabaseContext> options)
            : base(options)
        {
        }

        public DbSet<Game> Game { get; set; } = default!;
    }
}
