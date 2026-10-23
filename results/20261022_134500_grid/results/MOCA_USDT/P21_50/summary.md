# EMA Hourly Continuation — MOCA/USDT P21_50

**Symbol:** MOCA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 871 |
| net_profit_factor | 0.5249 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.9042 |
| gross_win_rate | 0.4661 |
| sharpe_ratio | -7.0776 |
| sortino_ratio | -3.0964 |
| max_drawdown | 0.9698 |
| cagr | -0.7788 |
| net_avg_win | 27.2757 |
| net_avg_loss | -42.5258 |
| avg_hold_time_bars | 4.4489 |
| exposure | 0.1943 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
