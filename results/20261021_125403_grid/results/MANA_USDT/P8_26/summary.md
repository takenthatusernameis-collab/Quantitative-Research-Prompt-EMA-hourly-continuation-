# EMA Hourly Continuation — MANA/USDT P8_26

**Symbol:** MANA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 664 |
| net_profit_factor | 0.6833 |
| net_win_rate | 0.4819 |
| gross_profit_factor | 0.9501 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -3.2565 |
| sortino_ratio | -1.2016 |
| max_drawdown | 0.7503 |
| cagr | -0.4224 |
| net_avg_win | 50.4287 |
| net_avg_loss | -68.6564 |
| avg_hold_time_bars | 6.5241 |
| exposure | 0.1969 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
