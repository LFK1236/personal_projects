using Game_Database.Services;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace Game_Database.Pages
{
    public class CollectionModel : PageModel
    {
        public List<Models.Game> games = new();

        private readonly ILogger<CollectionModel> _logger;

        public CollectionModel(ILogger<CollectionModel> logger)
        {
            _logger = logger;
        }

        public void OnGet()
        {
            games = GameService.GetAll();
        }
    }
}