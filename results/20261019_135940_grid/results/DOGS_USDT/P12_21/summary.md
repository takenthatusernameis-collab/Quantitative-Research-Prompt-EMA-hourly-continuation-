# EMA Hourly Continuation — DOGS/USDT P12_21

**Symbol:** DOGS/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1333 |
| net_profit_factor | 0.3275 |
| net_win_rate | 0.4051 |
| gross_profit_factor | 0.6904 |
| gross_win_rate | 0.4254 |
| sharpe_ratio | -13.1170 |
| sortino_ratio | -7.3229 |
| max_drawdown | 0.9997 |
| cagr | -0.9770 |
| net_avg_win | 9.0165 |
| net_avg_loss | -18.7465 |
| avg_hold_time_bars | 1.9857 |
| exposure | 0.1404 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
