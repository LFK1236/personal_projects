using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.EntityFrameworkCore;
using GameDatabase.Models;
using Microsoft.AspNetCore.Mvc.Rendering;

namespace GameDatabase.Pages.Games
{
    public class IndexModel : PageModel
    {
        private readonly GameDatabase.Data.GameDatabaseContext _context;

        public IndexModel(GameDatabase.Data.GameDatabaseContext context)
        {
            _context = context;
        }

        public IList<Game> GameList { get;set; } = default!;

        [BindProperty(SupportsGet = true)]
        public string? TitleSearchString { get; set; }

        [BindProperty(SupportsGet = true)]
        public string? DeveloperSearchString { get; set; }

        [BindProperty(SupportsGet = true)]
        public string? PublisherSearchString { get; set; }

        [BindProperty(SupportsGet = true)]
        public string? ReleaseYearSearchString { get; set; }

        [BindProperty(SupportsGet = true)]
        public string? RatingSearchString { get; set; }

        public SelectList? Genres { get; set; }

        [BindProperty(SupportsGet = true)]
        public string ? GameGenre { get; set; }

        public async Task OnGetAsync()
        {
            if (_context.Game != null)
            {
                var games = from g in _context.Game
                    select g;

                IQueryable<string> releaseQuery = from g in _context.Game
                    orderby g.Genre
                    select g.Genre;

                if (!string.IsNullOrEmpty(TitleSearchString))
                    games = games.Where(s => s.Title.Contains(TitleSearchString));

                if (!string.IsNullOrEmpty(DeveloperSearchString))
                    games = games.Where(s => s.Developer.Contains(DeveloperSearchString));

                if (!string.IsNullOrEmpty(PublisherSearchString))
                    games = games.Where(s => s.Publisher.Contains(PublisherSearchString));

                if (!string.IsNullOrEmpty(ReleaseYearSearchString))
                    games = games.Where(s => s.ReleaseYear.Contains(ReleaseYearSearchString));

                if (!string.IsNullOrEmpty(RatingSearchString))
                    games = games.Where(s => s.Rating.Equals(RatingSearchString));

                if (!string.IsNullOrEmpty(GameGenre))
                    games = games.Where(x => x.Genre == GameGenre);

                GameList = await games.ToListAsync();
                Genres = new SelectList(await releaseQuery.Distinct().ToListAsync());
            }
        }
    }
}
