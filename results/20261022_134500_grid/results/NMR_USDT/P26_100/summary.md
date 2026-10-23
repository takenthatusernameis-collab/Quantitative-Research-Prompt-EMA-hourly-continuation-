# EMA Hourly Continuation — NMR/USDT P26_100

**Symbol:** NMR/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.6594 |
| net_win_rate | 0.4742 |
| gross_profit_factor | 0.9926 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -4.2611 |
| sortino_ratio | -1.5849 |
| max_drawdown | 0.8579 |
| cagr | -0.5304 |
| net_avg_win | 49.7291 |
| net_avg_loss | -68.0166 |
| avg_hold_time_bars | 12.1748 |
| exposure | 0.3863 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
