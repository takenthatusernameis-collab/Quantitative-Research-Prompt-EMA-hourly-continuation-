# EMA Hourly Continuation — WOO/USDT P21_200

**Symbol:** WOO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.7600 |
| net_win_rate | 0.4985 |
| gross_profit_factor | 1.0165 |
| gross_win_rate | 0.5045 |
| sharpe_ratio | -1.6243 |
| sortino_ratio | -0.4171 |
| max_drawdown | 0.4055 |
| cagr | -0.1798 |
| net_avg_win | 75.2316 |
| net_avg_loss | -98.3962 |
| avg_hold_time_bars | 43.6435 |
| exposure | 0.6566 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
