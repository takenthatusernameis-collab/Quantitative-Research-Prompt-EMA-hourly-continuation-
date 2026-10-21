# EMA Hourly Continuation — ALGO/USDT P55_100

**Symbol:** ALGO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.8594 |
| net_win_rate | 0.5426 |
| gross_profit_factor | 1.1721 |
| gross_win_rate | 0.5426 |
| sharpe_ratio | -0.7817 |
| sortino_ratio | -0.2016 |
| max_drawdown | 0.2424 |
| cagr | -0.0900 |
| net_avg_win | 75.0010 |
| net_avg_loss | -103.5162 |
| avg_hold_time_bars | 8.0820 |
| exposure | 0.1165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
