# EMA Hourly Continuation — VR/USDT P8_26

**Symbol:** VR/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.7023 |
| net_win_rate | 0.4765 |
| gross_profit_factor | 0.9711 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -2.8728 |
| sortino_ratio | -0.9013 |
| max_drawdown | 0.6535 |
| cagr | -0.3443 |
| net_avg_win | 66.1563 |
| net_avg_loss | -85.7383 |
| avg_hold_time_bars | 10.4642 |
| exposure | 0.2326 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
