# EMA Hourly Continuation — RIO/USDT P144_200

**Symbol:** RIO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 174 |
| net_profit_factor | 0.5674 |
| net_win_rate | 0.3966 |
| gross_profit_factor | 0.6734 |
| gross_win_rate | 0.3966 |
| sharpe_ratio | -2.4389 |
| sortino_ratio | -0.4548 |
| max_drawdown | 0.4136 |
| cagr | -0.1901 |
| net_avg_win | 77.5258 |
| net_avg_loss | -89.7941 |
| avg_hold_time_bars | 7.5460 |
| exposure | 0.0603 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
