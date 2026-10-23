# EMA Hourly Continuation — VR/USDT P20_200

**Symbol:** VR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.4881 |
| net_win_rate | 0.3313 |
| gross_profit_factor | 0.7250 |
| gross_win_rate | 0.3415 |
| sharpe_ratio | -8.5040 |
| sortino_ratio | -2.6189 |
| max_drawdown | 0.9787 |
| cagr | -0.7814 |
| net_avg_win | 57.5771 |
| net_avg_loss | -58.4338 |
| avg_hold_time_bars | 28.6462 |
| exposure | 0.6367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
