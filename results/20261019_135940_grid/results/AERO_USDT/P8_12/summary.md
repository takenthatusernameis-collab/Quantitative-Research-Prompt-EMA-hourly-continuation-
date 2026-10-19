# EMA Hourly Continuation — AERO/USDT P8_12

**Symbol:** AERO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1774 |
| net_profit_factor | 0.1719 |
| net_win_rate | 0.3766 |
| gross_profit_factor | 0.4485 |
| gross_win_rate | 0.4138 |
| sharpe_ratio | -16.7397 |
| sortino_ratio | -10.0930 |
| max_drawdown | 1.0000 |
| cagr | -0.9956 |
| net_avg_win | 3.1066 |
| net_avg_loss | -10.9179 |
| avg_hold_time_bars | 1.8061 |
| exposure | 0.1456 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
