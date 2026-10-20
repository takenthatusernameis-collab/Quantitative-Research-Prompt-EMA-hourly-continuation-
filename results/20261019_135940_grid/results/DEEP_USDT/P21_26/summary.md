# EMA Hourly Continuation — DEEP/USDT P21_26

**Symbol:** DEEP/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 864 |
| net_profit_factor | 0.4304 |
| net_win_rate | 0.4062 |
| gross_profit_factor | 0.8283 |
| gross_win_rate | 0.4363 |
| sharpe_ratio | -10.9585 |
| sortino_ratio | -5.0641 |
| max_drawdown | 0.9956 |
| cagr | -0.9320 |
| net_avg_win | 21.4283 |
| net_avg_loss | -34.0682 |
| avg_hold_time_bars | 1.9028 |
| exposure | 0.0931 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
