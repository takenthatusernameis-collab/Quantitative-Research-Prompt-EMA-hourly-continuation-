# EMA Hourly Continuation — MOVR/USDT P50_200

**Symbol:** MOVR/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.5440 |
| net_win_rate | 0.4265 |
| gross_profit_factor | 0.7999 |
| gross_win_rate | 0.4361 |
| sharpe_ratio | -4.0553 |
| sortino_ratio | -1.1482 |
| max_drawdown | 0.7716 |
| cagr | -0.4308 |
| net_avg_win | 51.0208 |
| net_avg_loss | -69.7544 |
| avg_hold_time_bars | 20.3349 |
| exposure | 0.3836 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
