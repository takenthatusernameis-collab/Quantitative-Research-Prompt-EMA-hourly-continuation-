# EMA Hourly Continuation — MANA/USDT P50_100

**Symbol:** MANA/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.4320 |
| net_win_rate | 0.4141 |
| gross_profit_factor | 0.7843 |
| gross_win_rate | 0.4380 |
| sharpe_ratio | -7.2789 |
| sortino_ratio | -2.6397 |
| max_drawdown | 0.9659 |
| cagr | -0.7381 |
| net_avg_win | 26.5123 |
| net_avg_loss | -43.3622 |
| avg_hold_time_bars | 5.5022 |
| exposure | 0.1673 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
