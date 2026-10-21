# EMA Hourly Continuation — FLR/USDT P20_50

**Symbol:** FLR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.5517 |
| net_win_rate | 0.4391 |
| gross_profit_factor | 0.7770 |
| gross_win_rate | 0.4410 |
| sharpe_ratio | -4.4136 |
| sortino_ratio | -1.4653 |
| max_drawdown | 0.8298 |
| cagr | -0.4884 |
| net_avg_win | 42.1075 |
| net_avg_loss | -59.7492 |
| avg_hold_time_bars | 7.0037 |
| exposure | 0.1725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
