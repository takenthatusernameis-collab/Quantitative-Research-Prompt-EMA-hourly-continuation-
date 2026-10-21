# EMA Hourly Continuation — PROM/USDT P20_34

**Symbol:** PROM/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.4773 |
| net_win_rate | 0.4232 |
| gross_profit_factor | 0.7518 |
| gross_win_rate | 0.4254 |
| sharpe_ratio | -4.8891 |
| sortino_ratio | -1.4852 |
| max_drawdown | 0.8389 |
| cagr | -0.5037 |
| net_avg_win | 39.1661 |
| net_avg_loss | -60.2191 |
| avg_hold_time_bars | 5.2675 |
| exposure | 0.1092 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
