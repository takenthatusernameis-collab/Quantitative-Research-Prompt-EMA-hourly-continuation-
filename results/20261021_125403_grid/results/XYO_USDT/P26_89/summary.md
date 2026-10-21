# EMA Hourly Continuation — XYO/USDT P26_89

**Symbol:** XYO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.6374 |
| net_win_rate | 0.4478 |
| gross_profit_factor | 0.8471 |
| gross_win_rate | 0.4478 |
| sharpe_ratio | -3.4244 |
| sortino_ratio | -1.0527 |
| max_drawdown | 0.7165 |
| cagr | -0.3845 |
| net_avg_win | 59.0894 |
| net_avg_loss | -75.1700 |
| avg_hold_time_bars | 13.6738 |
| exposure | 0.2902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
