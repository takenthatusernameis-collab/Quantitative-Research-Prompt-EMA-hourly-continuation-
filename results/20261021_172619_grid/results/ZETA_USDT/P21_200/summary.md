# EMA Hourly Continuation — ZETA/USDT P21_200

**Symbol:** ZETA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.9835 |
| net_win_rate | 0.5356 |
| gross_profit_factor | 1.1523 |
| gross_win_rate | 0.5356 |
| sharpe_ratio | -0.0433 |
| sortino_ratio | -0.0102 |
| max_drawdown | 0.2484 |
| cagr | -0.0097 |
| net_avg_win | 101.5903 |
| net_avg_loss | -119.1199 |
| avg_hold_time_bars | 53.4157 |
| exposure | 0.6454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
