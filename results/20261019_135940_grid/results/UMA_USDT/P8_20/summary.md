# EMA Hourly Continuation — UMA/USDT P8_20

**Symbol:** UMA/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1580 |
| net_profit_factor | 0.3296 |
| net_win_rate | 0.4127 |
| gross_profit_factor | 0.7512 |
| gross_win_rate | 0.4424 |
| sharpe_ratio | -12.0977 |
| sortino_ratio | -6.8236 |
| max_drawdown | 0.9998 |
| cagr | -0.9669 |
| net_avg_win | 7.5388 |
| net_avg_loss | -16.0704 |
| avg_hold_time_bars | 3.3557 |
| exposure | 0.2410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
