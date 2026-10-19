# EMA Hourly Continuation — IOTA/USDT P12_89

**Symbol:** IOTA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 774 |
| net_profit_factor | 0.5620 |
| net_win_rate | 0.4522 |
| gross_profit_factor | 0.9059 |
| gross_win_rate | 0.4638 |
| sharpe_ratio | -5.1282 |
| sortino_ratio | -1.9908 |
| max_drawdown | 0.9197 |
| cagr | -0.6210 |
| net_avg_win | 33.4522 |
| net_avg_loss | -49.1361 |
| avg_hold_time_bars | 14.9548 |
| exposure | 0.5261 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
