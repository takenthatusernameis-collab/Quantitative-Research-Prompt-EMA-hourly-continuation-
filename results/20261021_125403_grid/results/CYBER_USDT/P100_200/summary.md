# EMA Hourly Continuation — CYBER/USDT P100_200

**Symbol:** CYBER/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.7091 |
| net_win_rate | 0.4804 |
| gross_profit_factor | 0.9073 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -1.7220 |
| sortino_ratio | -0.4121 |
| max_drawdown | 0.3789 |
| cagr | -0.1727 |
| net_avg_win | 68.3971 |
| net_avg_loss | -89.1930 |
| avg_hold_time_bars | 13.8221 |
| exposure | 0.1765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
