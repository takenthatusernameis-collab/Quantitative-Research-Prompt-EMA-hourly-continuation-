# EMA Hourly Continuation — DGB/USDT P8_20

**Symbol:** DGB/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.8345 |
| net_win_rate | 0.5316 |
| gross_profit_factor | 1.1767 |
| gross_win_rate | 0.5316 |
| sharpe_ratio | -1.4867 |
| sortino_ratio | -0.4758 |
| max_drawdown | 0.5264 |
| cagr | -0.1967 |
| net_avg_win | 81.7389 |
| net_avg_loss | -111.1538 |
| avg_hold_time_bars | 5.4521 |
| exposure | 0.1217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
