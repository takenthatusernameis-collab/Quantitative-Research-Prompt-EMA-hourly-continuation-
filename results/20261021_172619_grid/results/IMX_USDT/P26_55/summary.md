# EMA Hourly Continuation — IMX/USDT P26_55

**Symbol:** IMX/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.8358 |
| net_win_rate | 0.5236 |
| gross_profit_factor | 1.0924 |
| gross_win_rate | 0.5236 |
| sharpe_ratio | -1.1742 |
| sortino_ratio | -0.3648 |
| max_drawdown | 0.4097 |
| cagr | -0.1554 |
| net_avg_win | 72.3788 |
| net_avg_loss | -95.1746 |
| avg_hold_time_bars | 6.5215 |
| exposure | 0.1375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
