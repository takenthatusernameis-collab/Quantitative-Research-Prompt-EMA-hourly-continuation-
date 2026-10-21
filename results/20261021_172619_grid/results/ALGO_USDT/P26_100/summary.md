# EMA Hourly Continuation — ALGO/USDT P26_100

**Symbol:** ALGO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.8706 |
| net_win_rate | 0.5258 |
| gross_profit_factor | 1.1050 |
| gross_win_rate | 0.5258 |
| sharpe_ratio | -0.9158 |
| sortino_ratio | -0.2784 |
| max_drawdown | 0.3315 |
| cagr | -0.1225 |
| net_avg_win | 80.4358 |
| net_avg_loss | -102.4647 |
| avg_hold_time_bars | 15.0876 |
| exposure | 0.3052 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
