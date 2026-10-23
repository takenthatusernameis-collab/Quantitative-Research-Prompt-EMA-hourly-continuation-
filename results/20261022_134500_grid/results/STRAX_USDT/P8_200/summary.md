# EMA Hourly Continuation — STRAX/USDT P8_200

**Symbol:** STRAX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.5856 |
| net_win_rate | 0.4344 |
| gross_profit_factor | 0.8649 |
| gross_win_rate | 0.4455 |
| sharpe_ratio | -5.0261 |
| sortino_ratio | -1.7771 |
| max_drawdown | 0.8817 |
| cagr | -0.5747 |
| net_avg_win | 45.3100 |
| net_avg_loss | -59.4331 |
| avg_hold_time_bars | 23.8231 |
| exposure | 0.6895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
