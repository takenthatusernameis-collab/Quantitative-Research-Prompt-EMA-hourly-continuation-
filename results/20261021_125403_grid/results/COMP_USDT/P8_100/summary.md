# EMA Hourly Continuation — COMP/USDT P8_100

**Symbol:** COMP/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.7829 |
| net_win_rate | 0.5068 |
| gross_profit_factor | 1.0121 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -1.5329 |
| sortino_ratio | -0.4631 |
| max_drawdown | 0.4459 |
| cagr | -0.1922 |
| net_avg_win | 66.4934 |
| net_avg_loss | -87.2589 |
| avg_hold_time_bars | 35.0653 |
| exposure | 0.7077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
