# EMA Hourly Continuation — SAND/USDT P8_55

**Symbol:** SAND/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.6811 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 0.8722 |
| gross_win_rate | 0.4607 |
| sharpe_ratio | -3.2798 |
| sortino_ratio | -1.2003 |
| max_drawdown | 0.7579 |
| cagr | -0.4238 |
| net_avg_win | 52.4932 |
| net_avg_loss | -65.8424 |
| avg_hold_time_bars | 15.5740 |
| exposure | 0.4686 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
