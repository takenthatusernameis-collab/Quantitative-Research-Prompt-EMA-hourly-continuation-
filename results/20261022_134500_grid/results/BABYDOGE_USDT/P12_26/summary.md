# EMA Hourly Continuation — BABYDOGE/USDT P12_26

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 28 |
| net_profit_factor | 1.2032 |
| net_win_rate | 0.5714 |
| gross_profit_factor | 1.3220 |
| gross_win_rate | 0.5714 |
| sharpe_ratio | 0.3201 |
| sortino_ratio | 0.0248 |
| max_drawdown | 0.0306 |
| cagr | 0.0101 |
| net_avg_win | 95.2590 |
| net_avg_loss | -105.5623 |
| avg_hold_time_bars | 6.2857 |
| exposure | 0.0080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
