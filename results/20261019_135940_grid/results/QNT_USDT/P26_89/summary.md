# EMA Hourly Continuation — QNT/USDT P26_89

**Symbol:** QNT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 867 |
| net_profit_factor | 0.5076 |
| net_win_rate | 0.4694 |
| gross_profit_factor | 0.9098 |
| gross_win_rate | 0.4844 |
| sharpe_ratio | -5.8078 |
| sortino_ratio | -2.3998 |
| max_drawdown | 0.9502 |
| cagr | -0.6907 |
| net_avg_win | 24.0008 |
| net_avg_loss | -41.8329 |
| avg_hold_time_bars | 7.2191 |
| exposure | 0.2845 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
