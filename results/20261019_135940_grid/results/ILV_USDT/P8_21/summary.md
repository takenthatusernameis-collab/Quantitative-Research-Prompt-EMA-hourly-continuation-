# EMA Hourly Continuation — ILV/USDT P8_21

**Symbol:** ILV/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1632 |
| net_profit_factor | 0.3367 |
| net_win_rate | 0.4412 |
| gross_profit_factor | 0.7597 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -10.9383 |
| sortino_ratio | -6.2345 |
| max_drawdown | 0.9996 |
| cagr | -0.9553 |
| net_avg_win | 7.0470 |
| net_avg_loss | -16.5239 |
| avg_hold_time_bars | 3.0625 |
| exposure | 0.2272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
