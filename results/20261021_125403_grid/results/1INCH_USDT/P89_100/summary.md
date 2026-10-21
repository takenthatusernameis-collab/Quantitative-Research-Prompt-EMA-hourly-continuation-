# EMA Hourly Continuation — 1INCH/USDT P89_100

**Symbol:** 1INCH/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 120 |
| net_profit_factor | 0.4333 |
| net_win_rate | 0.4083 |
| gross_profit_factor | 0.6715 |
| gross_win_rate | 0.4083 |
| sharpe_ratio | -2.7155 |
| sortino_ratio | -0.4270 |
| max_drawdown | 0.4042 |
| cagr | -0.1804 |
| net_avg_win | 61.3701 |
| net_avg_loss | -97.7367 |
| avg_hold_time_bars | 4.4833 |
| exposure | 0.0245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
