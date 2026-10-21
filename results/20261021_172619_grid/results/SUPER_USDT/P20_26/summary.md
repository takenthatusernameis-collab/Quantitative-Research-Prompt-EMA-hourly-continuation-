# EMA Hourly Continuation — SUPER/USDT P20_26

**Symbol:** SUPER/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 232 |
| net_profit_factor | 0.6975 |
| net_win_rate | 0.5086 |
| gross_profit_factor | 1.0727 |
| gross_win_rate | 0.5216 |
| sharpe_ratio | -1.7151 |
| sortino_ratio | -0.3746 |
| max_drawdown | 0.3722 |
| cagr | -0.1589 |
| net_avg_win | 68.8514 |
| net_avg_loss | -102.1801 |
| avg_hold_time_bars | 4.3147 |
| exposure | 0.0455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
