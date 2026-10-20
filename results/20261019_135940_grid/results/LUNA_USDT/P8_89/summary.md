# EMA Hourly Continuation — LUNA/USDT P8_89

**Symbol:** LUNA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 922 |
| net_profit_factor | 0.5278 |
| net_win_rate | 0.4403 |
| gross_profit_factor | 0.8722 |
| gross_win_rate | 0.4490 |
| sharpe_ratio | -7.0569 |
| sortino_ratio | -2.9941 |
| max_drawdown | 0.9778 |
| cagr | -0.7776 |
| net_avg_win | 26.8968 |
| net_avg_loss | -40.0982 |
| avg_hold_time_bars | 13.7679 |
| exposure | 0.5770 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
