# EMA Hourly Continuation — LUNA/USDT P50_100

**Symbol:** LUNA/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 725 |
| net_profit_factor | 0.4039 |
| net_win_rate | 0.4317 |
| gross_profit_factor | 0.7737 |
| gross_win_rate | 0.4483 |
| sharpe_ratio | -7.2164 |
| sortino_ratio | -2.7473 |
| max_drawdown | 0.9689 |
| cagr | -0.7460 |
| net_avg_win | 20.9542 |
| net_avg_loss | -39.4141 |
| avg_hold_time_bars | 5.0979 |
| exposure | 0.1680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
