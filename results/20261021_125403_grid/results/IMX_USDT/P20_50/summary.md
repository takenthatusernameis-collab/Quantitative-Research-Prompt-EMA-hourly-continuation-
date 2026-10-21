# EMA Hourly Continuation — IMX/USDT P20_50

**Symbol:** IMX/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.7711 |
| net_win_rate | 0.5028 |
| gross_profit_factor | 0.9985 |
| gross_win_rate | 0.5028 |
| sharpe_ratio | -1.7931 |
| sortino_ratio | -0.5904 |
| max_drawdown | 0.5098 |
| cagr | -0.2377 |
| net_avg_win | 62.7747 |
| net_avg_loss | -82.3397 |
| avg_hold_time_bars | 7.5728 |
| exposure | 0.1813 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
