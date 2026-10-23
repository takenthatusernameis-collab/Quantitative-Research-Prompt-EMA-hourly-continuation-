# EMA Hourly Continuation — DODO/USDT P12_20

**Symbol:** DODO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1535 |
| net_profit_factor | 0.3315 |
| net_win_rate | 0.3974 |
| gross_profit_factor | 0.8178 |
| gross_win_rate | 0.4274 |
| sharpe_ratio | -13.2065 |
| sortino_ratio | -7.3461 |
| max_drawdown | 0.9999 |
| cagr | -0.9757 |
| net_avg_win | 8.1287 |
| net_avg_loss | -16.1704 |
| avg_hold_time_bars | 2.4932 |
| exposure | 0.1732 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
