# EMA Hourly Continuation — MANA/USDT P8_12

**Symbol:** MANA/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1841 |
| net_profit_factor | 0.1735 |
| net_win_rate | 0.3493 |
| gross_profit_factor | 0.7486 |
| gross_win_rate | 0.4030 |
| sharpe_ratio | -19.3741 |
| sortino_ratio | -12.0969 |
| max_drawdown | 1.0000 |
| cagr | -0.9987 |
| net_avg_win | 3.2636 |
| net_avg_loss | -10.0989 |
| avg_hold_time_bars | 1.7197 |
| exposure | 0.1439 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
