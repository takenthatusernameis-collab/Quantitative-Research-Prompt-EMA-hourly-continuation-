# EMA Hourly Continuation — SUI/USDT P12_50

**Symbol:** SUI/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1109 |
| net_profit_factor | 0.5732 |
| net_win_rate | 0.4436 |
| gross_profit_factor | 0.9337 |
| gross_win_rate | 0.4581 |
| sharpe_ratio | -7.6435 |
| sortino_ratio | -3.5616 |
| max_drawdown | 0.9882 |
| cagr | -0.8291 |
| net_avg_win | 26.9759 |
| net_avg_loss | -37.5263 |
| avg_hold_time_bars | 6.5789 |
| exposure | 0.3316 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
