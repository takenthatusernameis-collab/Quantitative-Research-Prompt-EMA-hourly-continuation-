# EMA Hourly Continuation — CSPR/USDT P50_144

**Symbol:** CSPR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.6170 |
| net_win_rate | 0.4347 |
| gross_profit_factor | 0.7736 |
| gross_win_rate | 0.4347 |
| sharpe_ratio | -2.9812 |
| sortino_ratio | -0.8413 |
| max_drawdown | 0.6249 |
| cagr | -0.3215 |
| net_avg_win | 57.9683 |
| net_avg_loss | -72.2376 |
| avg_hold_time_bars | 14.4925 |
| exposure | 0.2622 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
