# EMA Hourly Continuation — ENA/USDT P21_34

**Symbol:** ENA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1142 |
| net_profit_factor | 0.4391 |
| net_win_rate | 0.4431 |
| gross_profit_factor | 0.7625 |
| gross_win_rate | 0.4510 |
| sharpe_ratio | -8.2124 |
| sortino_ratio | -3.9313 |
| max_drawdown | 0.9922 |
| cagr | -0.8520 |
| net_avg_win | 15.3411 |
| net_avg_loss | -27.7988 |
| avg_hold_time_bars | 2.4694 |
| exposure | 0.1282 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
