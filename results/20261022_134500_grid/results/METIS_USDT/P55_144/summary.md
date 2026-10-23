# EMA Hourly Continuation — METIS/USDT P55_144

**Symbol:** METIS/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.5163 |
| net_win_rate | 0.4360 |
| gross_profit_factor | 0.8072 |
| gross_win_rate | 0.4438 |
| sharpe_ratio | -4.6636 |
| sortino_ratio | -1.4901 |
| max_drawdown | 0.8386 |
| cagr | -0.5127 |
| net_avg_win | 39.6452 |
| net_avg_loss | -59.3681 |
| avg_hold_time_bars | 10.7597 |
| exposure | 0.2524 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
