# EMA Hourly Continuation — VR/USDT P12_144

**Symbol:** VR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.7095 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.8400 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -1.9924 |
| sortino_ratio | -0.5242 |
| max_drawdown | 0.4598 |
| cagr | -0.2174 |
| net_avg_win | 70.6222 |
| net_avg_loss | -84.6345 |
| avg_hold_time_bars | 37.7486 |
| exposure | 0.5937 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
