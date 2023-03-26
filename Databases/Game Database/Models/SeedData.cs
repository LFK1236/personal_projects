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
                /*
                                context.Developer.AddRange(
                                    new Developer("id Software"),
                                    new Developer("Santa Monica Studio"),
                                    new Developer("Ember Lab"),
                                    new Developer("Blizzard Entertainment")
                                );

                                context.Genre.AddRange(
                                    new Genre("FPS"),
                                    new Genre("Action-Adventure"),
                                    new Genre("MMORPG")
                                );

                                context.Platform.AddRange(
                                    new Platform("Windows", "PC"),
                                    new Platform("Playstation 5", "PS5"),
                                    new Platform("Playstation 4", "PS4"),
                                    new Platform("Playstation 3", "PS3"),
                                    new Platform("Playstation 2", "PS2"),
                                    new Platform("Playstation 1", "PSX"),
                                    new Platform("Xbox", "Xbox"),
                                    new Platform("Xbox 360", "360"),
                                    new Platform("Xbox Original", "OG Xbox"),
                                    new Platform("Nintendo Switch", "Switch"),
                                    new Platform("Nintendo Wii U", "WiiU"),
                                    new Platform("Nintendo Wii", "Wii"),
                                    new Platform("Nintendo new 3DS", "N3DS"),
                                    new Platform("Nintendo 3DS", "3DS"),
                                    new Platform("Nintendo DS", "DS"),
                                    new Platform("Nintendo GameCube", "GC"),
                                    new Platform("Nintendo 64", "N64"),
                                    new Platform("Super Nintendo Entertainment System", "SNES"),
                                    new Platform("Nintendo Entertainment System", "NES")
                                );

                                context.Publisher.AddRange(
                                    new Publisher("Bethesda Softworks", "Bethesda"),
                                    new Publisher("Sony Interactive Entertainment", "Sony"),
                                    new Publisher("Ember Lab"),
                                    new Publisher("Blizzard Entertainment", "Blizzard")
                                );

                                context.Tag.AddRange(
                                    new Tag("First Person"),
                                    new Tag("Shooter"),
                                    new Tag("Violent"),
                                    new Tag("Singleplayer"),
                                    new Tag("Multiplayer"),
                                    new Tag("MMORPG"),
                                    new Tag("Exploration"),
                                    new Tag("Story-Rich"),
                                    new Tag("Emotional"),
                                    new Tag("Third Person"),
                                    new Tag("RPG"),
                                    new Tag("Open World"),
                                    new Tag("Indie"),
                                    new Tag("Top-Down"),
                                    new Tag("Strategy"),
                                    new Tag("Turn-based"),
                                    new Tag("Real-time"),
                                    new Tag("4X"),
                                    new Tag("Slice of Life"),
                                    new Tag("Casual")
                                );
                */
                context.Game.AddRange(
                    new Game("Doom", 2016)
                    {
                        Genre = "FPS",
                        Developer = "id Software",
                        Publisher = "Bethesda Softworks"
                    },

                    new Game("God of War", 2018)
                    {
                        Genre = "Action-Adventure",
                        Developer = "Santa Monica Studio",
                        Publisher = "Sony Interactive Entertainment"
                    },

                    new Game("Kena: Bridge of Spirits", 2021)
                    {
                        Genre = "Action-Adventure",
                        Developer = "Ember Lab",
                        Publisher = "Ember Lab"
                    },

                    new Game("World of Warcraft", 2004)
                    {
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