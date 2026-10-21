# EMA Hourly Continuation — ATH/USDT P12_200

**Symbol:** ATH/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 229 |
| net_profit_factor | 1.0923 |
| net_win_rate | 0.5590 |
| gross_profit_factor | 1.2431 |
| gross_win_rate | 0.5590 |
| sharpe_ratio | 0.4941 |
| sortino_ratio | 0.1123 |
| max_drawdown | 0.1284 |
| cagr | 0.0448 |
| net_avg_win | 100.4438 |
| net_avg_loss | -116.5412 |
| avg_hold_time_bars | 69.9651 |
| exposure | 0.7766 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
