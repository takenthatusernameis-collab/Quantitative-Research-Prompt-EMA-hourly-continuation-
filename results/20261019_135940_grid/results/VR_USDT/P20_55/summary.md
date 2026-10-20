# EMA Hourly Continuation — VR/USDT P20_55

**Symbol:** VR/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1000 |
| net_profit_factor | 0.4333 |
| net_win_rate | 0.3320 |
| gross_profit_factor | 0.6988 |
| gross_win_rate | 0.3500 |
| sharpe_ratio | -13.0050 |
| sortino_ratio | -5.7963 |
| max_drawdown | 0.9998 |
| cagr | -0.9648 |
| net_avg_win | 23.0254 |
| net_avg_loss | -26.4105 |
| avg_hold_time_bars | 5.7940 |
| exposure | 0.2634 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
