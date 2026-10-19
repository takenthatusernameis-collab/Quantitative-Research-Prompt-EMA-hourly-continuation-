# EMA Hourly Continuation — ZK/USDT P50_100

**Symbol:** ZK/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 629 |
| net_profit_factor | 0.5616 |
| net_win_rate | 0.4531 |
| gross_profit_factor | 0.9120 |
| gross_win_rate | 0.4642 |
| sharpe_ratio | -5.1595 |
| sortino_ratio | -1.8801 |
| max_drawdown | 0.8852 |
| cagr | -0.6000 |
| net_avg_win | 39.6886 |
| net_avg_loss | -58.5487 |
| avg_hold_time_bars | 6.0413 |
| exposure | 0.1853 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
