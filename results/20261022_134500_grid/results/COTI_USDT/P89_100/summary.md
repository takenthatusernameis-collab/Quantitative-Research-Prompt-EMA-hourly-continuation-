# EMA Hourly Continuation — COTI/USDT P89_100

**Symbol:** COTI/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 628 |
| net_profit_factor | 0.3012 |
| net_win_rate | 0.4092 |
| gross_profit_factor | 0.8055 |
| gross_win_rate | 0.4459 |
| sharpe_ratio | -8.6430 |
| sortino_ratio | -3.1048 |
| max_drawdown | 0.9826 |
| cagr | -0.7999 |
| net_avg_win | 16.4766 |
| net_avg_loss | -37.8937 |
| avg_hold_time_bars | 1.8217 |
| exposure | 0.0520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
