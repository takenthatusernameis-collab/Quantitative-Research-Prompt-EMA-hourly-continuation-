# EMA Hourly Continuation — BAND/USDT P20_26

**Symbol:** BAND/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.5610 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.8863 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -3.8921 |
| sortino_ratio | -1.1121 |
| max_drawdown | 0.7313 |
| cagr | -0.4022 |
| net_avg_win | 50.7507 |
| net_avg_loss | -77.0051 |
| avg_hold_time_bars | 4.7563 |
| exposure | 0.0857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
