# EMA Hourly Continuation — MOVR/USDT P21_26

**Symbol:** MOVR/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1232 |
| net_profit_factor | 0.1960 |
| net_win_rate | 0.3636 |
| gross_profit_factor | 0.6217 |
| gross_win_rate | 0.4156 |
| sharpe_ratio | -14.2388 |
| sortino_ratio | -7.2461 |
| max_drawdown | 0.9999 |
| cagr | -0.9783 |
| net_avg_win | 5.4419 |
| net_avg_loss | -15.8639 |
| avg_hold_time_bars | 2.1266 |
| exposure | 0.1191 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
