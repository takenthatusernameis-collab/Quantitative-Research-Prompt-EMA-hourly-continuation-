# EMA Hourly Continuation — MOCA/USDT P144_200

**Symbol:** MOCA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.4560 |
| net_win_rate | 0.4442 |
| gross_profit_factor | 0.8507 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -5.3738 |
| sortino_ratio | -1.5691 |
| max_drawdown | 0.8340 |
| cagr | -0.5419 |
| net_avg_win | 40.7359 |
| net_avg_loss | -71.3806 |
| avg_hold_time_bars | 4.0416 |
| exposure | 0.0780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
