# EMA Hourly Continuation — W/USDT P8_26

**Symbol:** W/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.8306 |
| net_win_rate | 0.5196 |
| gross_profit_factor | 1.0689 |
| gross_win_rate | 0.5196 |
| sharpe_ratio | -1.4968 |
| sortino_ratio | -0.5659 |
| max_drawdown | 0.5065 |
| cagr | -0.2311 |
| net_avg_win | 66.1606 |
| net_avg_loss | -86.1531 |
| avg_hold_time_bars | 6.6778 |
| exposure | 0.2091 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
