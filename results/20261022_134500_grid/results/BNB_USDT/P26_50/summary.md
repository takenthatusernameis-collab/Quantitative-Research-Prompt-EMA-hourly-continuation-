# EMA Hourly Continuation — BNB/USDT P26_50

**Symbol:** BNB/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 963 |
| net_profit_factor | 0.2175 |
| net_win_rate | 0.3811 |
| gross_profit_factor | 0.7590 |
| gross_win_rate | 0.4548 |
| sharpe_ratio | -12.8034 |
| sortino_ratio | -5.8141 |
| max_drawdown | 0.9996 |
| cagr | -0.9559 |
| net_avg_win | 7.5702 |
| net_avg_loss | -21.4334 |
| avg_hold_time_bars | 3.6147 |
| exposure | 0.1582 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
