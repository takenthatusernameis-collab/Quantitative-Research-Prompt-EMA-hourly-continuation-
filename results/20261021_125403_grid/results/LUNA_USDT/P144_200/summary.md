# EMA Hourly Continuation — LUNA/USDT P144_200

**Symbol:** LUNA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 196 |
| net_profit_factor | 0.6811 |
| net_win_rate | 0.4898 |
| gross_profit_factor | 0.9334 |
| gross_win_rate | 0.4898 |
| sharpe_ratio | -1.5666 |
| sortino_ratio | -0.3144 |
| max_drawdown | 0.3411 |
| cagr | -0.1343 |
| net_avg_win | 67.5608 |
| net_avg_loss | -95.2322 |
| avg_hold_time_bars | 9.0459 |
| exposure | 0.0806 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
