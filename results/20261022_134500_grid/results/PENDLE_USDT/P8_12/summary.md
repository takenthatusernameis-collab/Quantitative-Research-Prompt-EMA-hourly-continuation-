# EMA Hourly Continuation — PENDLE/USDT P8_12

**Symbol:** PENDLE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1768 |
| net_profit_factor | 0.2786 |
| net_win_rate | 0.3835 |
| gross_profit_factor | 0.7749 |
| gross_win_rate | 0.4265 |
| sharpe_ratio | -15.9450 |
| sortino_ratio | -9.5724 |
| max_drawdown | 1.0000 |
| cagr | -0.9935 |
| net_avg_win | 5.6973 |
| net_avg_loss | -12.7181 |
| avg_hold_time_bars | 1.9055 |
| exposure | 0.1531 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
