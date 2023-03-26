using GameDatabase.Models;

namespace GameDatabase.Services
{
    public static class GameService
    {
        static List<Game> Games { get; }
        static GameService()
        {
            Games = new List<Game>
            {
                new Game ("Star Wars Jedi: Fallen Order", 2019),
                new Game ("Kena: Bridge of Spirits", 2021)
            };
        }

        public static List<Game> GetAll() => Games;

        public static Game? Get(string title, int release) => Games.FirstOrDefault(g => g.Title == title && g.ReleaseYear == release);

        public static void Add(Game game) => Games.Add(game);

        public static void Delete(string title, int release)
        {
            var game = Get(title, release);
            if (game is null)
                return;

            Games.Remove(game);
        }
    }
}
