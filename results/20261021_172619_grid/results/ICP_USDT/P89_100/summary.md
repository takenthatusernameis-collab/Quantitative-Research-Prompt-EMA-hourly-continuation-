# EMA Hourly Continuation — ICP/USDT P89_100

**Symbol:** ICP/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 85 |
| net_profit_factor | 0.8024 |
| net_win_rate | 0.5294 |
| gross_profit_factor | 1.1120 |
| gross_win_rate | 0.5294 |
| sharpe_ratio | -0.5998 |
| sortino_ratio | -0.0799 |
| max_drawdown | 0.1080 |
| cagr | -0.0362 |
| net_avg_win | 79.7698 |
| net_avg_loss | -111.8370 |
| avg_hold_time_bars | 5.2000 |
| exposure | 0.0201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
