# EMA Hourly Continuation — BLZ/USDT P8_34

**Symbol:** BLZ/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1379 |
| net_profit_factor | 0.4974 |
| net_win_rate | 0.4155 |
| gross_profit_factor | 0.8456 |
| gross_win_rate | 0.4300 |
| sharpe_ratio | -9.6940 |
| sortino_ratio | -5.0657 |
| max_drawdown | 0.9980 |
| cagr | -0.9143 |
| net_avg_win | 17.2355 |
| net_avg_loss | -24.6347 |
| avg_hold_time_bars | 6.0297 |
| exposure | 0.3763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
