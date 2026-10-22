# EMA Hourly Continuation — SAND/USDT P100_200

**Symbol:** SAND/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.5712 |
| net_win_rate | 0.4738 |
| gross_profit_factor | 0.9296 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -3.3234 |
| sortino_ratio | -0.9161 |
| max_drawdown | 0.6727 |
| cagr | -0.3536 |
| net_avg_win | 48.9931 |
| net_avg_loss | -77.2384 |
| avg_hold_time_bars | 8.9005 |
| exposure | 0.1545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
