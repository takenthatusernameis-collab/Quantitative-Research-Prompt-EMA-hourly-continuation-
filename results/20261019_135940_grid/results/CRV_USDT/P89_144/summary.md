# EMA Hourly Continuation — CRV/USDT P89_144

**Symbol:** CRV/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 553 |
| net_profit_factor | 0.4498 |
| net_win_rate | 0.4430 |
| gross_profit_factor | 0.7577 |
| gross_win_rate | 0.4503 |
| sharpe_ratio | -5.2985 |
| sortino_ratio | -1.7518 |
| max_drawdown | 0.8863 |
| cagr | -0.5755 |
| net_avg_win | 29.4912 |
| net_avg_loss | -52.1523 |
| avg_hold_time_bars | 4.4123 |
| exposure | 0.1109 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
