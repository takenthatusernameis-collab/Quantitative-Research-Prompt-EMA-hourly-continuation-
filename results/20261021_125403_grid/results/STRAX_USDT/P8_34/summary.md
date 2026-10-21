# EMA Hourly Continuation — STRAX/USDT P8_34

**Symbol:** STRAX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 841 |
| net_profit_factor | 0.5701 |
| net_win_rate | 0.4423 |
| gross_profit_factor | 0.7979 |
| gross_win_rate | 0.4435 |
| sharpe_ratio | -5.3688 |
| sortino_ratio | -2.2206 |
| max_drawdown | 0.9249 |
| cagr | -0.6418 |
| net_avg_win | 32.9078 |
| net_avg_loss | -45.7808 |
| avg_hold_time_bars | 8.1379 |
| exposure | 0.3129 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
