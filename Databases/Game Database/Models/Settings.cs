namespace GameDatabase.Models
{
    public static class Settings
    {
        public enum SortCategories {Title, ReleaseYear, Genre, Developer, Publisher, Platform, Rating}
        public enum SortDirections { Asc, Des }
        public static SortCategories SortCategory { get; set; } = SortCategories.Title;
        public static SortDirections SortDirection { get; set; } = SortDirections.Asc;
    }
}
