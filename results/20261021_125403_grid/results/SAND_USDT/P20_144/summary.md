# EMA Hourly Continuation — SAND/USDT P20_144

**Symbol:** SAND/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.6738 |
| net_win_rate | 0.4451 |
| gross_profit_factor | 0.8363 |
| gross_win_rate | 0.4451 |
| sharpe_ratio | -2.6299 |
| sortino_ratio | -0.7108 |
| max_drawdown | 0.5775 |
| cagr | -0.2795 |
| net_avg_win | 71.5104 |
| net_avg_loss | -85.1188 |
| avg_hold_time_bars | 31.5687 |
| exposure | 0.5223 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
