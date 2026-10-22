# EMA Hourly Continuation — ZBCN/USDT P50_89

**Symbol:** ZBCN/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 766 |
| net_profit_factor | 0.4986 |
| net_win_rate | 0.4399 |
| gross_profit_factor | 0.8374 |
| gross_win_rate | 0.4530 |
| sharpe_ratio | -6.0488 |
| sortino_ratio | -2.3772 |
| max_drawdown | 0.9461 |
| cagr | -0.6838 |
| net_avg_win | 27.7881 |
| net_avg_loss | -43.7777 |
| avg_hold_time_bars | 3.4739 |
| exposure | 0.1231 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
