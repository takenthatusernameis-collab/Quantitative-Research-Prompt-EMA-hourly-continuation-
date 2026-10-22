# EMA Hourly Continuation — MTL/USDT P50_55

**Symbol:** MTL/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 246 |
| net_profit_factor | 0.4557 |
| net_win_rate | 0.4228 |
| gross_profit_factor | 0.7666 |
| gross_win_rate | 0.4228 |
| sharpe_ratio | -4.0194 |
| sortino_ratio | -0.9059 |
| max_drawdown | 0.6664 |
| cagr | -0.3446 |
| net_avg_win | 52.7789 |
| net_avg_loss | -84.8188 |
| avg_hold_time_bars | 7.8455 |
| exposure | 0.0873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
