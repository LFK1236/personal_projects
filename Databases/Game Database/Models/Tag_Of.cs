namespace GameDatabase.Models
{
    public class Tag_Of
    {
        public Game Game { get; set; }
        public Tag Tag { get; set; }

        public Tag_Of(Game game, Tag tag)
        {
            Game = game;
            Tag = tag;
        }
    }
}
