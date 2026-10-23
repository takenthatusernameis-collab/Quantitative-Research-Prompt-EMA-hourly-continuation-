# EMA Hourly Continuation — RLC/USDT P50_144

**Symbol:** RLC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.5671 |
| net_win_rate | 0.4588 |
| gross_profit_factor | 0.8809 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -3.8622 |
| sortino_ratio | -1.2125 |
| max_drawdown | 0.7759 |
| cagr | -0.4414 |
| net_avg_win | 44.1426 |
| net_avg_loss | -65.9759 |
| avg_hold_time_bars | 13.1730 |
| exposure | 0.2976 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
