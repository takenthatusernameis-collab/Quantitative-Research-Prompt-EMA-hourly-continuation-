# EMA Hourly Continuation — FLOW/USDT P8_20

**Symbol:** FLOW/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.5693 |
| net_win_rate | 0.4641 |
| gross_profit_factor | 0.8357 |
| gross_win_rate | 0.4641 |
| sharpe_ratio | -4.0237 |
| sortino_ratio | -1.4251 |
| max_drawdown | 0.8052 |
| cagr | -0.4787 |
| net_avg_win | 37.4713 |
| net_avg_loss | -56.9941 |
| avg_hold_time_bars | 4.9167 |
| exposure | 0.1368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
