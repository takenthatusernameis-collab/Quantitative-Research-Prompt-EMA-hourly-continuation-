# EMA Hourly Continuation — OGN/USDT P8_55

**Symbol:** OGN/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 711 |
| net_profit_factor | 0.7403 |
| net_win_rate | 0.4880 |
| gross_profit_factor | 0.9718 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -2.7588 |
| sortino_ratio | -1.0478 |
| max_drawdown | 0.7071 |
| cagr | -0.3818 |
| net_avg_win | 57.7420 |
| net_avg_loss | -74.3509 |
| avg_hold_time_bars | 14.8186 |
| exposure | 0.4768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
