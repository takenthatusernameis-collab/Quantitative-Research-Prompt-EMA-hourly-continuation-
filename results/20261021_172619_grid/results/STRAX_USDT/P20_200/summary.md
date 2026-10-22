# EMA Hourly Continuation — STRAX/USDT P20_200

**Symbol:** STRAX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.5621 |
| net_win_rate | 0.4201 |
| gross_profit_factor | 0.7195 |
| gross_win_rate | 0.4201 |
| sharpe_ratio | -3.8310 |
| sortino_ratio | -1.1593 |
| max_drawdown | 0.7383 |
| cagr | -0.4155 |
| net_avg_win | 49.3590 |
| net_avg_loss | -63.6239 |
| avg_hold_time_bars | 25.9562 |
| exposure | 0.5423 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
