﻿using Newtonsoft.Json;

namespace JWT
{
    public class JwtTokenConfig
    {
        [JsonProperty("secret")]
        public string Secret { get; set; }

        [JsonProperty("issuer")]
        public string Issuer { get; set; }

        [JsonProperty("audience")]
        public string Audience { get; set; }

        [JsonProperty("accessTokenExpiration")]
        public int AccessTokenExpiration { get; set; }

        [JsonProperty("refreshTokenExpiration")]
        public int RefreshTokenExpiration { get; set; }
    }
}
