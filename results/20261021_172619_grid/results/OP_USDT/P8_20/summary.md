# EMA Hourly Continuation — OP/USDT P8_20

**Symbol:** OP/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.8139 |
| net_win_rate | 0.5327 |
| gross_profit_factor | 1.1127 |
| gross_win_rate | 0.5327 |
| sharpe_ratio | -1.3111 |
| sortino_ratio | -0.4324 |
| max_drawdown | 0.4565 |
| cagr | -0.1809 |
| net_avg_win | 62.2331 |
| net_avg_loss | -87.1645 |
| avg_hold_time_bars | 5.3385 |
| exposure | 0.1262 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
