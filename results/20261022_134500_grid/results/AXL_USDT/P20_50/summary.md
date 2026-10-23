# EMA Hourly Continuation — AXL/USDT P20_50

**Symbol:** AXL/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1086 |
| net_profit_factor | 0.5343 |
| net_win_rate | 0.4217 |
| gross_profit_factor | 0.8847 |
| gross_win_rate | 0.4291 |
| sharpe_ratio | -8.0533 |
| sortino_ratio | -3.7260 |
| max_drawdown | 0.9896 |
| cagr | -0.8353 |
| net_avg_win | 24.7884 |
| net_avg_loss | -33.8335 |
| avg_hold_time_bars | 4.7182 |
| exposure | 0.2319 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
