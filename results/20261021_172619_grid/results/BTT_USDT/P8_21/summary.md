# EMA Hourly Continuation — BTT/USDT P8_21

**Symbol:** BTT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 552 |
| net_profit_factor | 0.4713 |
| net_win_rate | 0.4149 |
| gross_profit_factor | 0.8194 |
| gross_win_rate | 0.4149 |
| sharpe_ratio | -6.9392 |
| sortino_ratio | -2.3643 |
| max_drawdown | 0.9413 |
| cagr | -0.6736 |
| net_avg_win | 36.5810 |
| net_avg_loss | -55.0341 |
| avg_hold_time_bars | 6.7681 |
| exposure | 0.1698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
