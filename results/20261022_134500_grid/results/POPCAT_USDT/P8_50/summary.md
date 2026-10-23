# EMA Hourly Continuation — POPCAT/USDT P8_50

**Symbol:** POPCAT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 930 |
| net_profit_factor | 0.6358 |
| net_win_rate | 0.4548 |
| gross_profit_factor | 0.8631 |
| gross_win_rate | 0.4602 |
| sharpe_ratio | -5.4543 |
| sortino_ratio | -2.5254 |
| max_drawdown | 0.9261 |
| cagr | -0.6994 |
| net_avg_win | 38.1904 |
| net_avg_loss | -50.1180 |
| avg_hold_time_bars | 9.8312 |
| exposure | 0.4830 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
