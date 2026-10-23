# EMA Hourly Continuation — BLZ/USDT P20_100

**Symbol:** BLZ/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 734 |
| net_profit_factor | 0.5775 |
| net_win_rate | 0.4237 |
| gross_profit_factor | 0.8668 |
| gross_win_rate | 0.4332 |
| sharpe_ratio | -5.8957 |
| sortino_ratio | -2.2386 |
| max_drawdown | 0.9366 |
| cagr | -0.6587 |
| net_avg_win | 41.0306 |
| net_avg_loss | -52.2374 |
| avg_hold_time_bars | 13.0681 |
| exposure | 0.4341 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
