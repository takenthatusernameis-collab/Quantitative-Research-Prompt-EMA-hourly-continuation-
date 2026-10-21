# EMA Hourly Continuation — DODO/USDT P20_100

**Symbol:** DODO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.7454 |
| net_win_rate | 0.4761 |
| gross_profit_factor | 0.9323 |
| gross_win_rate | 0.4761 |
| sharpe_ratio | -2.2671 |
| sortino_ratio | -0.7065 |
| max_drawdown | 0.6249 |
| cagr | -0.2771 |
| net_avg_win | 71.4669 |
| net_avg_loss | -87.1261 |
| avg_hold_time_bars | 19.3825 |
| exposure | 0.4219 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
