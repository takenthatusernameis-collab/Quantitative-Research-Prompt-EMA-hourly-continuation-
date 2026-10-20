# EMA Hourly Continuation — PEOPLE/USDT P12_26

**Symbol:** PEOPLE/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1366 |
| net_profit_factor | 0.4066 |
| net_win_rate | 0.4165 |
| gross_profit_factor | 0.7081 |
| gross_win_rate | 0.4275 |
| sharpe_ratio | -10.0621 |
| sortino_ratio | -5.2375 |
| max_drawdown | 0.9985 |
| cagr | -0.9234 |
| net_avg_win | 12.0261 |
| net_avg_loss | -21.1136 |
| avg_hold_time_bars | 3.2284 |
| exposure | 0.1996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
