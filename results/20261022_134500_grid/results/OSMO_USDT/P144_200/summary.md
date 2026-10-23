# EMA Hourly Continuation — OSMO/USDT P144_200

**Symbol:** OSMO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.4800 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.8774 |
| gross_win_rate | 0.4587 |
| sharpe_ratio | -4.2338 |
| sortino_ratio | -1.1342 |
| max_drawdown | 0.7442 |
| cagr | -0.4144 |
| net_avg_win | 43.1779 |
| net_avg_loss | -73.6462 |
| avg_hold_time_bars | 4.5043 |
| exposure | 0.0719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
