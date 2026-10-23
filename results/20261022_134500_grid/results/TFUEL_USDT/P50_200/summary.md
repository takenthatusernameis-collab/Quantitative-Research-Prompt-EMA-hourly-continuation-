# EMA Hourly Continuation — TFUEL/USDT P50_200

**Symbol:** TFUEL/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.4495 |
| net_win_rate | 0.3738 |
| gross_profit_factor | 0.7126 |
| gross_win_rate | 0.3928 |
| sharpe_ratio | -6.3848 |
| sortino_ratio | -2.0530 |
| max_drawdown | 0.9224 |
| cagr | -0.6343 |
| net_avg_win | 38.1714 |
| net_avg_loss | -50.6952 |
| avg_hold_time_bars | 14.8178 |
| exposure | 0.3534 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
