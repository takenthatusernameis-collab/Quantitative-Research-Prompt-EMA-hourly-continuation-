# EMA Hourly Continuation — BDX/USDT P8_55

**Symbol:** BDX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.4384 |
| net_win_rate | 0.3660 |
| gross_profit_factor | 0.6666 |
| gross_win_rate | 0.3695 |
| sharpe_ratio | -7.1765 |
| sortino_ratio | -2.4517 |
| max_drawdown | 0.9501 |
| cagr | -0.6852 |
| net_avg_win | 35.2994 |
| net_avg_loss | -46.4885 |
| avg_hold_time_bars | 8.2119 |
| exposure | 0.2131 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
