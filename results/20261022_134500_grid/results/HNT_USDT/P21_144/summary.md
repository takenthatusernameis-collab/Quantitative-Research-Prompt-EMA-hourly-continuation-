# EMA Hourly Continuation — HNT/USDT P21_144

**Symbol:** HNT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.6346 |
| net_win_rate | 0.4580 |
| gross_profit_factor | 0.8488 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -3.4215 |
| sortino_ratio | -1.1073 |
| max_drawdown | 0.7476 |
| cagr | -0.4059 |
| net_avg_win | 52.7854 |
| net_avg_loss | -70.2937 |
| avg_hold_time_bars | 22.8683 |
| exposure | 0.5447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
