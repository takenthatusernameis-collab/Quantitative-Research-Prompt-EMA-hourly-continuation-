# EMA Hourly Continuation — ARKM/USDT P50_144

**Symbol:** ARKM/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.7023 |
| net_win_rate | 0.4972 |
| gross_profit_factor | 0.9974 |
| gross_win_rate | 0.5047 |
| sharpe_ratio | -2.5284 |
| sortino_ratio | -0.8268 |
| max_drawdown | 0.6350 |
| cagr | -0.3233 |
| net_avg_win | 55.4283 |
| net_avg_loss | -78.0407 |
| avg_hold_time_bars | 10.9495 |
| exposure | 0.2663 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
