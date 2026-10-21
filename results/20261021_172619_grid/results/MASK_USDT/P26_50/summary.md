# EMA Hourly Continuation — MASK/USDT P26_50

**Symbol:** MASK/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.5775 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.8950 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -3.6757 |
| sortino_ratio | -1.1544 |
| max_drawdown | 0.7474 |
| cagr | -0.4159 |
| net_avg_win | 44.2246 |
| net_avg_loss | -68.7659 |
| avg_hold_time_bars | 6.4855 |
| exposure | 0.1427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
