# EMA Hourly Continuation — XYO/USDT P12_20

**Symbol:** XYO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1588 |
| net_profit_factor | 0.2357 |
| net_win_rate | 0.3495 |
| gross_profit_factor | 0.7711 |
| gross_win_rate | 0.3892 |
| sharpe_ratio | -16.8355 |
| sortino_ratio | -9.7201 |
| max_drawdown | 1.0000 |
| cagr | -0.9939 |
| net_avg_win | 5.5571 |
| net_avg_loss | -12.6662 |
| avg_hold_time_bars | 2.5094 |
| exposure | 0.1803 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
