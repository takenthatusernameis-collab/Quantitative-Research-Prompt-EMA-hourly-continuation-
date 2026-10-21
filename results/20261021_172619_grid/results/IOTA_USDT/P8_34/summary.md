# EMA Hourly Continuation — IOTA/USDT P8_34

**Symbol:** IOTA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 798 |
| net_profit_factor | 0.7141 |
| net_win_rate | 0.4862 |
| gross_profit_factor | 0.9518 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -3.1149 |
| sortino_ratio | -1.2587 |
| max_drawdown | 0.7764 |
| cagr | -0.4389 |
| net_avg_win | 49.2917 |
| net_avg_loss | -65.3231 |
| avg_hold_time_bars | 8.3421 |
| exposure | 0.3026 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
