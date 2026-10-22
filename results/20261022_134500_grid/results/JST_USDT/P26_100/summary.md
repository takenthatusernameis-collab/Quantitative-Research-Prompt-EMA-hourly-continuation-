# EMA Hourly Continuation — JST/USDT P26_100

**Symbol:** JST/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.3496 |
| net_win_rate | 0.4541 |
| gross_profit_factor | 0.9648 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -6.3502 |
| sortino_ratio | -2.1644 |
| max_drawdown | 0.9454 |
| cagr | -0.6806 |
| net_avg_win | 18.3180 |
| net_avg_loss | -43.5800 |
| avg_hold_time_bars | 12.1279 |
| exposure | 0.3348 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
