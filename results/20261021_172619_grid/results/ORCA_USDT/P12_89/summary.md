# EMA Hourly Continuation — ORCA/USDT P12_89

**Symbol:** ORCA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.8198 |
| net_win_rate | 0.5102 |
| gross_profit_factor | 1.0146 |
| gross_win_rate | 0.5102 |
| sharpe_ratio | -1.2650 |
| sortino_ratio | -0.4007 |
| max_drawdown | 0.4308 |
| cagr | -0.1711 |
| net_avg_win | 68.4111 |
| net_avg_loss | -86.9227 |
| avg_hold_time_bars | 24.9367 |
| exposure | 0.5554 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
