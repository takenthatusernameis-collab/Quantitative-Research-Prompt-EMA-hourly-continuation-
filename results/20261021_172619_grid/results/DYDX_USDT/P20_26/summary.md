# EMA Hourly Continuation — DYDX/USDT P20_26

**Symbol:** DYDX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 201 |
| net_profit_factor | 0.7432 |
| net_win_rate | 0.5075 |
| gross_profit_factor | 1.0348 |
| gross_win_rate | 0.5075 |
| sharpe_ratio | -1.3258 |
| sortino_ratio | -0.2704 |
| max_drawdown | 0.2846 |
| cagr | -0.1159 |
| net_avg_win | 75.4905 |
| net_avg_loss | -104.6532 |
| avg_hold_time_bars | 4.7114 |
| exposure | 0.0430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
