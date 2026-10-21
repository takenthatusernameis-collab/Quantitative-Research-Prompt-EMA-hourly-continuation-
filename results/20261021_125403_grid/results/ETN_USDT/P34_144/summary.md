# EMA Hourly Continuation — ETN/USDT P34_144

**Symbol:** ETN/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.6183 |
| net_win_rate | 0.4377 |
| gross_profit_factor | 0.7633 |
| gross_win_rate | 0.4377 |
| sharpe_ratio | -2.9812 |
| sortino_ratio | -0.8565 |
| max_drawdown | 0.5927 |
| cagr | -0.3267 |
| net_avg_win | 60.5491 |
| net_avg_loss | -76.2234 |
| avg_hold_time_bars | 16.4290 |
| exposure | 0.3079 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
