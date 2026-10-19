# EMA Hourly Continuation — RAY/USDT P20_100

**Symbol:** RAY/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.6243 |
| net_win_rate | 0.4619 |
| gross_profit_factor | 0.8831 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -4.0685 |
| sortino_ratio | -1.4637 |
| max_drawdown | 0.8422 |
| cagr | -0.5041 |
| net_avg_win | 45.4145 |
| net_avg_loss | -62.4431 |
| avg_hold_time_bars | 13.0091 |
| exposure | 0.3879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
