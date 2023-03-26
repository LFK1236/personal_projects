using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Mvc.Rendering;
using GameDatabase.Data;
using GameDatabase.Models;
using Org.BouncyCastle.Asn1.X509;

namespace GameDatabase.Pages.Games
{
    public class IndexModel : PageModel
    {
        private readonly GameDatabaseContext _context;

        public IndexModel(GameDatabaseContext context)
        {
            _context = context;
        }

        public IList<Game> GameList { get; set; } = default!;

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

        [BindProperty(SupportsGet = true)]
        public string? PlatformSearchString { get; set; }

        public SelectList? Genres { get; set; }

        [BindProperty(SupportsGet = true)]
        public string? GameGenre { get; set; }

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
                    games = games.Where(g => g.Title.Contains(TitleSearchString));

                if (!string.IsNullOrEmpty(DeveloperSearchString))
                    games = games.Where(g => g.Developer.Contains(DeveloperSearchString));

                if (!string.IsNullOrEmpty(PublisherSearchString))
                    games = games.Where(g => g.Publisher.Contains(PublisherSearchString));

                if (!string.IsNullOrEmpty(ReleaseYearSearchString))
                    games = games.Where(g => g.ReleaseYear.Equals(ReleaseYearSearchString));

                if (!string.IsNullOrEmpty(RatingSearchString))
                    games = games.Where(g => g.Rating.Equals(RatingSearchString));

                if (!string.IsNullOrEmpty(PlatformSearchString))
                    games = games.Where(g => g.Platform.Contains(PlatformSearchString));

                if (!string.IsNullOrEmpty(GameGenre))
                    games = games.Where(g => g.Genre.Contains(GameGenre));

                var SortCategory = Settings.SortCategory;
                var SortDirection = Settings.SortDirection;
                if (SortDirection == Settings.SortDirections.Asc)
                {
                    switch (SortCategory)
                    {
                        case Settings.SortCategories.ReleaseYear:
                            games = games.OrderBy(g => g.ReleaseYear);
                            break;
                        case Settings.SortCategories.Genre:
                            games = games.OrderBy(g => g.Genre);
                            break;
                        case Settings.SortCategories.Developer:
                            games = games.OrderBy(g => g.Developer);
                            break;
                        case Settings.SortCategories.Publisher:
                            games = games.OrderBy(g => g.Publisher);
                            break;
                        case Settings.SortCategories.Platform:
                            games = games.OrderBy(g => g.Platform);
                            break;
                        case Settings.SortCategories.Rating:
                            games = games.OrderBy(g => g.Rating);
                            break;
                        default:
                            games = games.OrderBy(g => g.Title);
                            break;
                    }
                }
                else
                {
                    switch (SortCategory)
                    {
                        case Settings.SortCategories.ReleaseYear:
                            games = games.OrderByDescending(g => g.ReleaseYear);
                            break;
                        case Settings.SortCategories.Genre:
                            games = games.OrderByDescending(g => g.Genre);
                            break;
                        case Settings.SortCategories.Developer:
                            games = games.OrderByDescending(g => g.Developer);
                            break;
                        case Settings.SortCategories.Publisher:
                            games = games.OrderByDescending(g => g.Publisher);
                            break;
                        case Settings.SortCategories.Platform:
                            games = games.OrderByDescending(g => g.Platform);
                            break;
                        case Settings.SortCategories.Rating:
                            games = games.OrderByDescending(g => g.Rating);
                            break;
                        default:
                            games = games.OrderByDescending(g => g.Title);
                            break;
                    }
                }

                GameList = await games.ToListAsync();
                Genres = new SelectList(await releaseQuery.Distinct().ToListAsync());
            }
        }
        
        
        // Sort
        public async Task<IActionResult> OnGetSort(Settings.SortCategories category)
        {            
            if (category == Settings.SortCategory)
            {
                if (Settings.SortDirection == Settings.SortDirections.Asc)
                    Settings.SortDirection = Settings.SortDirections.Des;
                else
                    Settings.SortDirection = Settings.SortDirections.Asc;
            }
            else
            {
                Settings.SortCategory = category;
            }
            
            return RedirectToPage("./Index");
        }
    }
}
