# EMA Hourly Continuation — HNT/USDT P50_200

**Symbol:** HNT/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.6418 |
| net_win_rate | 0.4411 |
| gross_profit_factor | 0.7558 |
| gross_win_rate | 0.4411 |
| sharpe_ratio | -2.3304 |
| sortino_ratio | -0.5987 |
| max_drawdown | 0.5236 |
| cagr | -0.2416 |
| net_avg_win | 61.4421 |
| net_avg_loss | -75.5508 |
| avg_hold_time_bars | 26.3021 |
| exposure | 0.3957 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
