# EMA Hourly Continuation — SWFTC/USDT P8_12

**Symbol:** SWFTC/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1736 |
| net_profit_factor | 0.1346 |
| net_win_rate | 0.3168 |
| gross_profit_factor | 0.4137 |
| gross_win_rate | 0.3698 |
| sharpe_ratio | -19.4454 |
| sortino_ratio | -11.8317 |
| max_drawdown | 1.0000 |
| cagr | -0.9986 |
| net_avg_win | 2.8281 |
| net_avg_loss | -9.7432 |
| avg_hold_time_bars | 1.9533 |
| exposure | 0.1541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
