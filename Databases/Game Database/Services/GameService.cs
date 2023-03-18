using Game_Database.Models;
using System.Collections.Generic;
using System.Linq;

namespace Game_Database.Services
{
    public static class GameService
    {
        static List<Game> Games { get; }
        static GameService()
        {
            Games = new List<Game>
            {
                new Game { Title = "Star Wars Jedi: Fallen Order", Release = "2019" },
                new Game { Title = "Kena: Bridge of Spirits", Release = "2021" }
            };
        }

        public static List<Game> GetAll() => Games;

        public static Game? Get(string title, string release) => Games.FirstOrDefault(g => (g.Title == title) && (g.Release == release));

        public static void Add(Game game) => Games.Add(game);

        public static void Delete(string title, string release)
        {
            var game = Get(title, release);
            if (game is null)
                return;

            Games.Remove(game);
        }
    }
}
