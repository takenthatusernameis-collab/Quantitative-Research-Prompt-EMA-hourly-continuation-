# EMA Hourly Continuation — GRT/USDT P20_100

**Symbol:** GRT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.8155 |
| net_win_rate | 0.5032 |
| gross_profit_factor | 1.0103 |
| gross_win_rate | 0.5032 |
| sharpe_ratio | -1.4273 |
| sortino_ratio | -0.4407 |
| max_drawdown | 0.4500 |
| cagr | -0.1845 |
| net_avg_win | 75.6369 |
| net_avg_loss | -93.9480 |
| avg_hold_time_bars | 18.2741 |
| exposure | 0.3862 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
