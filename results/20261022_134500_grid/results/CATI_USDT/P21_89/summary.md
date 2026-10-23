# EMA Hourly Continuation — CATI/USDT P21_89

**Symbol:** CATI/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.5709 |
| net_win_rate | 0.4515 |
| gross_profit_factor | 0.8756 |
| gross_win_rate | 0.4653 |
| sharpe_ratio | -5.5635 |
| sortino_ratio | -2.1873 |
| max_drawdown | 0.8996 |
| cagr | -0.6530 |
| net_avg_win | 40.3945 |
| net_avg_loss | -58.2366 |
| avg_hold_time_bars | 11.6133 |
| exposure | 0.4131 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
