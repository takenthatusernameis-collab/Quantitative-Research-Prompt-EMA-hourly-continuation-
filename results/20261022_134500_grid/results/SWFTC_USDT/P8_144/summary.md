# EMA Hourly Continuation — SWFTC/USDT P8_144

**Symbol:** SWFTC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 717 |
| net_profit_factor | 0.5833 |
| net_win_rate | 0.4296 |
| gross_profit_factor | 0.8744 |
| gross_win_rate | 0.4379 |
| sharpe_ratio | -5.6593 |
| sortino_ratio | -2.1164 |
| max_drawdown | 0.9272 |
| cagr | -0.6466 |
| net_avg_win | 42.1046 |
| net_avg_loss | -54.3626 |
| avg_hold_time_bars | 19.7699 |
| exposure | 0.6443 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
