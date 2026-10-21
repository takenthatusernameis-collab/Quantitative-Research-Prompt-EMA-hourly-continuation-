# EMA Hourly Continuation — BTT/USDT P20_50

**Symbol:** BTT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.4991 |
| net_win_rate | 0.4249 |
| gross_profit_factor | 0.8357 |
| gross_win_rate | 0.4249 |
| sharpe_ratio | -5.7983 |
| sortino_ratio | -1.8072 |
| max_drawdown | 0.8822 |
| cagr | -0.5732 |
| net_avg_win | 44.4000 |
| net_avg_loss | -65.7197 |
| avg_hold_time_bars | 8.9549 |
| exposure | 0.1897 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
