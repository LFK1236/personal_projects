namespace GameDatabase.Models
{
    public class Tag
    {
        public string TagName { get; set; }

        public Tag(string tagName)
        {
            TagName = tagName;
        }
    }
}
