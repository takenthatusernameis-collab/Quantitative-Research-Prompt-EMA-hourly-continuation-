# EMA Hourly Continuation — SUPER/USDT P12_144

**Symbol:** SUPER/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.7296 |
| net_win_rate | 0.4950 |
| gross_profit_factor | 1.0200 |
| gross_win_rate | 0.5091 |
| sharpe_ratio | -2.1765 |
| sortino_ratio | -0.6863 |
| max_drawdown | 0.6093 |
| cagr | -0.2769 |
| net_avg_win | 61.0879 |
| net_avg_loss | -82.0639 |
| avg_hold_time_bars | 29.6539 |
| exposure | 0.6699 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
