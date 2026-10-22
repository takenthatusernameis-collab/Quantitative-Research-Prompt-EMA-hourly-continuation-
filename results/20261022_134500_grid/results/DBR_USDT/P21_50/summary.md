# EMA Hourly Continuation — DBR/USDT P21_50

**Symbol:** DBR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 630 |
| net_profit_factor | 0.5214 |
| net_win_rate | 0.4460 |
| gross_profit_factor | 0.9883 |
| gross_win_rate | 0.4730 |
| sharpe_ratio | -6.7994 |
| sortino_ratio | -2.6974 |
| max_drawdown | 0.9348 |
| cagr | -0.7315 |
| net_avg_win | 35.9943 |
| net_avg_loss | -55.5882 |
| avg_hold_time_bars | 7.2365 |
| exposure | 0.2593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
