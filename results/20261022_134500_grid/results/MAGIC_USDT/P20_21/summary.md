# EMA Hourly Continuation — MAGIC/USDT P20_21

**Symbol:** MAGIC/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1157 |
| net_profit_factor | 0.2121 |
| net_win_rate | 0.3431 |
| gross_profit_factor | 0.8215 |
| gross_win_rate | 0.4296 |
| sharpe_ratio | -15.0715 |
| sortino_ratio | -7.5008 |
| max_drawdown | 1.0000 |
| cagr | -0.9837 |
| net_avg_win | 6.7793 |
| net_avg_loss | -16.6987 |
| avg_hold_time_bars | 2.3345 |
| exposure | 0.1228 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
