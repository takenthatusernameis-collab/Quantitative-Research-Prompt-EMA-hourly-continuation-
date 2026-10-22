# EMA Hourly Continuation — STX/USDT P20_100

**Symbol:** STX/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.6382 |
| net_win_rate | 0.4763 |
| gross_profit_factor | 0.9191 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -3.4740 |
| sortino_ratio | -1.1902 |
| max_drawdown | 0.7705 |
| cagr | -0.4300 |
| net_avg_win | 47.5693 |
| net_avg_loss | -67.7841 |
| avg_hold_time_bars | 17.2322 |
| exposure | 0.4601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
