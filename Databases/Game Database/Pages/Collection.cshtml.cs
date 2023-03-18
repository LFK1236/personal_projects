using Game_Database.Services;
using Game_Database.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace Game_Database.Pages
{
    public class CollectionModel : PageModel
    {
        public List<Models.Game> games = new();

        [BindProperty]
        public Game NewGame { get; set; } = new();

        private readonly ILogger<CollectionModel> _logger;

        public CollectionModel(ILogger<CollectionModel> logger)
        {
            _logger = logger;
        }

        public void OnGet()
        {
            games = GameService.GetAll();
        }

        public IActionResult OnPost()
        {
            if (!ModelState.IsValid) return Page();

            GameService.Add(NewGame);
            return RedirectToAction("Get");
        }

        public IActionResult OnPostDelete(string title, string release_year)
        {
            GameService.Delete(title, release_year);
            return RedirectToAction("Get");
        }
    }
}