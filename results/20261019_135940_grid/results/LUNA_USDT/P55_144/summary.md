# EMA Hourly Continuation — LUNA/USDT P55_144

**Symbol:** LUNA/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 570 |
| net_profit_factor | 0.4925 |
| net_win_rate | 0.4439 |
| gross_profit_factor | 0.8790 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -5.2491 |
| sortino_ratio | -1.7689 |
| max_drawdown | 0.8878 |
| cagr | -0.5748 |
| net_avg_win | 33.8837 |
| net_avg_loss | -54.9063 |
| avg_hold_time_bars | 9.9825 |
| exposure | 0.2586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
