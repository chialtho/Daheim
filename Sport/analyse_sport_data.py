#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import argparse as ap

def main():
    parser = ap.ArgumentParser(description="Analyse sport data")
    parser.add_argument("-f", type=str, required=True, help="Path to the Sport datas file")
    args = parser.parse_args()
    df = pd.read_csv(
        args.f,
        header=0,
        names=['month', 'day', 'type', 'distance', 'time', 'strength_training', 'distance_bike', 'time_bike'],
        dtype={
            'month': str,
            'day': str,
            'type': str,
            'distance': float,
            'time': str,
            'strength_training': float,
            'distance_bike': float,
            'time_bike': str
        }
    )

    def time_to_seconds(x):
        if isinstance(x, str) and ':' in x:
            return sum(int(i) * 60 ** idx for idx, i in enumerate(reversed(x.split(':'))))
        elif isinstance(x, str) and x.isdigit():
            return int(x) * 60
        else:
            return pd.NA

    df['time'] = df['time'].apply(time_to_seconds)
    df['time_bike'] = df['time_bike'].apply(time_to_seconds)

    sport_counts = df['type'].value_counts()
    # Add total to sport_counts
    sport_counts['Total'] = sport_counts.sum()
    
    df['distance_f'] = df.apply(lambda x: x['distance'] if x['type'] == 'F' else pd.NA, axis=1)
    df['distance_l'] = df.apply(lambda x: x['distance'] if x['type'] == 'L' else pd.NA, axis=1)
    total_distance_f = df['distance_f'].sum(skipna=True)
    total_distance_l = df['distance_l'].sum(skipna=True)
    total_distance_bike = df['distance_bike'].sum(skipna=True)
    total_time_strength = df['strength_training'].sum(skipna=True) # in minutes
    total_time_strength_str = f"{int(total_time_strength/60)}h {int(total_time_strength % 60):02d}min"

    df['distance'] = df['distance'] * 1000
    df['distance_bike'] = df['distance_bike'] * 1000

    df['speed_f'] = df.apply(lambda x: x['distance'] / x['time'] if x['type'] == 'F' and pd.notna(x['distance']) and pd.notna(x['time']) and x['time'] != 0 else pd.NA, axis=1)
    df['speed_l'] = df.apply(lambda x: x['distance'] / x['time'] if x['type'] == 'L' and pd.notna(x['distance']) and pd.notna(x['time']) and x['time'] != 0 else pd.NA, axis=1)
    df['speed_bike'] = df.apply(lambda x: x['distance_bike'] / x['time_bike'] if pd.notna(x['distance_bike']) and pd.notna(x['time_bike']) and x['time_bike'] != 0 else pd.NA, axis=1)

    avg_speed_f = df['speed_f'].mean(skipna=True) * 3.6
    avg_speed_l = df['speed_l'].mean(skipna=True) * 3.6
    avg_speed_bike = df['speed_bike'].mean(skipna=True) * 3.6

    df['speed_s'] = df.apply(lambda x: x['distance'] / x['time'] if x['type'] == 'S' and pd.notna(x['distance']) and pd.notna(x['time']) and x['time'] != 0 else pd.NA, axis=1)
    avg_speed_s = df['speed_s'].mean(skipna=True) * 3.6
    total_distance_s = df[df['type'] == 'S']['distance'].sum(skipna=True) / 1000

    # Write markdown output
    out_file_name = args.f.replace('.txt', '_report.md')

    with open(out_file_name, "w", encoding="utf-8") as f:
        f.write("# Sport Data Report\n\n")
        f.write("## Sport Counts\n")
        f.write(sport_counts.to_markdown() + "\n\n")
        f.write("## Summary\n")
        f.write(f"- **Total distance run on treadmill:** {total_distance_f:.2f} km\n")
        f.write(f"- **Total distance run outside:** {total_distance_l:.2f} km\n")
        f.write(f"- **Total distance cycled:** {total_distance_bike:.2f} km\n")
        f.write(f"- **Total distance swimming:** {total_distance_s:.2f} km\n")
        f.write(f"- **Total time spent on strength training:** {total_time_strength_str}\n\n")
        f.write("## Average Speeds\n")
        f.write(f"- **Treadmill running:** {avg_speed_f:.2f} km/h\n")
        f.write(f"- **Outside running:** {avg_speed_l:.2f} km/h\n")
        f.write(f"- **Cycling:** {avg_speed_bike:.2f} km/h\n")
        f.write(f"- **Swimming:** {avg_speed_s:.2f} km/h\n")

if __name__ == "__main__":
    main()