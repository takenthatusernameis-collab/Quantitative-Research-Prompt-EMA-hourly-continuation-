# EMA Hourly Continuation — XYO/USDT P12_20

**Symbol:** XYO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.4659 |
| net_win_rate | 0.4056 |
| gross_profit_factor | 0.7279 |
| gross_win_rate | 0.4056 |
| sharpe_ratio | -5.1301 |
| sortino_ratio | -1.4529 |
| max_drawdown | 0.8199 |
| cagr | -0.4916 |
| net_avg_win | 44.9087 |
| net_avg_loss | -65.7764 |
| avg_hold_time_bars | 5.2832 |
| exposure | 0.0937 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
