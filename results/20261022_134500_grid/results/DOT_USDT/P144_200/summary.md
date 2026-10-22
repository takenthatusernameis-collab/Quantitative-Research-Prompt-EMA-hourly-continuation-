# EMA Hourly Continuation — DOT/USDT P144_200

**Symbol:** DOT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.4396 |
| net_win_rate | 0.4432 |
| gross_profit_factor | 0.9264 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -5.1063 |
| sortino_ratio | -1.3819 |
| max_drawdown | 0.8344 |
| cagr | -0.5066 |
| net_avg_win | 39.7187 |
| net_avg_loss | -71.9296 |
| avg_hold_time_bars | 3.7946 |
| exposure | 0.0638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
