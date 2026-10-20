# EMA Hourly Continuation — VR/USDT P34_50

**Symbol:** VR/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 988 |
| net_profit_factor | 0.3252 |
| net_win_rate | 0.2692 |
| gross_profit_factor | 0.6298 |
| gross_win_rate | 0.3006 |
| sharpe_ratio | -16.2361 |
| sortino_ratio | -7.6099 |
| max_drawdown | 1.0000 |
| cagr | -0.9893 |
| net_avg_win | 18.1179 |
| net_avg_loss | -20.5253 |
| avg_hold_time_bars | 2.8775 |
| exposure | 0.1292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
