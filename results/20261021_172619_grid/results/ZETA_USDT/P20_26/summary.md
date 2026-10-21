# EMA Hourly Continuation — ZETA/USDT P20_26

**Symbol:** ZETA/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.5959 |
| net_win_rate | 0.4701 |
| gross_profit_factor | 0.8768 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -2.6213 |
| sortino_ratio | -0.6134 |
| max_drawdown | 0.5138 |
| cagr | -0.2435 |
| net_avg_win | 59.1390 |
| net_avg_loss | -88.0652 |
| avg_hold_time_bars | 4.4403 |
| exposure | 0.0538 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
