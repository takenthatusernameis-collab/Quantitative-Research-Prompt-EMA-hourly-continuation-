# EMA Hourly Continuation — SUSHI/USDT P34_100

**Symbol:** SUSHI/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.7868 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0004 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.5944 |
| sortino_ratio | -0.4815 |
| max_drawdown | 0.4547 |
| cagr | -0.1992 |
| net_avg_win | 70.9926 |
| net_avg_loss | -90.2308 |
| avg_hold_time_bars | 13.1233 |
| exposure | 0.2649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
