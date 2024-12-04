const MatchCard = ({ match }) => {
  return (
    <div className="match-card">
      <img src={match.profile_photo} alt={match.name} />
      <h3>{match.name}, {match.age}</h3>
      <div className="music-compatibility">
        <h4>Music Match: {match.compatibility_score}%</h4>
        <div className="common-artists">
          <h5>Common Artists</h5>
          {match.common_artists.map(artist => (
            <span key={artist.id}>{artist.name}</span>
          ))}
        </div>
      </div>
    </div>
  );
};