# EMA Hourly Continuation — AKT/USDT P34_100

**Symbol:** AKT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 405 |
| net_profit_factor | 0.8515 |
| net_win_rate | 0.5136 |
| gross_profit_factor | 1.0427 |
| gross_win_rate | 0.5136 |
| sharpe_ratio | -0.9421 |
| sortino_ratio | -0.2725 |
| max_drawdown | 0.2876 |
| cagr | -0.1201 |
| net_avg_win | 75.7459 |
| net_avg_loss | -93.9272 |
| avg_hold_time_bars | 12.1333 |
| exposure | 0.2234 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
