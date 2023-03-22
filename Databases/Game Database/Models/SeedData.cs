using Microsoft.EntityFrameworkCore;
using GameDatabase.Data;

namespace GameDatabase.Models
{
    public static class SeedData
    {
        public static void Initialise(IServiceProvider serviceProvider)
        {
            using (var context = new GameDatabaseContext(
                serviceProvider.GetRequiredService<DbContextOptions<GameDatabaseContext>>()))
            {
                if (context == null || context.Game == null)
                {
                    throw new ArgumentNullException("No GameDatabaseContext");
                }

                if (context.Game.Any()) return; // Database has already been seeded.

                context.Game.AddRange(
                    new Game
                    {
                        Title = "Doom",
                        ReleaseYear = "2016",
                        Genre = "FPS",
                        Developer = "id Software",
                        Publisher = "Bethesda Softworks"
                    },

                    new Game
                    {
                        Title = "God of War",
                        ReleaseYear = "2018",
                        Genre = "Action-Adventure",
                        Developer = "Santa Monica Studio",
                        Publisher = "Sony Interactive Entertainment"
                    },

                    new Game
                    {
                        Title = "Kena: Bridge of Spirits",
                        ReleaseYear = "2021",
                        Genre = "Action-Adventure",
                        Developer = "Ember Lab",
                        Publisher = "Ember Lab"
                    },

                    new Game
                    {
                        Title = "World of Warcraft",
                        ReleaseYear = "2004",
                        Genre = "MMORPG",
                        Developer = "Blizzard Entertainment",
                        Publisher = "Blizzard Entertainment"
                    }
                );
                context.SaveChanges();
            }
        }
    }
}