using System;

namespace Common
{
    public class RefreshToken : BaseEntity
    {
        public Guid UserId { set; get; }
        public User User { set; get; }

        public string TokenString { get; set; }
        public DateTime ExpireAt { get; set; }
    }
}
