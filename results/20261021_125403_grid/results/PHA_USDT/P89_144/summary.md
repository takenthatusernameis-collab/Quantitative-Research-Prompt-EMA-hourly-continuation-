# EMA Hourly Continuation — PHA/USDT P89_144

**Symbol:** PHA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.6911 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.8744 |
| gross_win_rate | 0.4727 |
| sharpe_ratio | -1.7958 |
| sortino_ratio | -0.4246 |
| max_drawdown | 0.4500 |
| cagr | -0.1774 |
| net_avg_win | 66.7269 |
| net_avg_loss | -86.5612 |
| avg_hold_time_bars | 7.5709 |
| exposure | 0.0946 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
