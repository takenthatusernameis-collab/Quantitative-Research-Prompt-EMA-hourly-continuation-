# EMA Hourly Continuation — ZETA/USDT P34_200

**Symbol:** ZETA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.8002 |
| net_win_rate | 0.5117 |
| gross_profit_factor | 1.0834 |
| gross_win_rate | 0.5175 |
| sharpe_ratio | -1.3636 |
| sortino_ratio | -0.3560 |
| max_drawdown | 0.4336 |
| cagr | -0.1564 |
| net_avg_win | 79.8446 |
| net_avg_loss | -104.5621 |
| avg_hold_time_bars | 34.4561 |
| exposure | 0.5332 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
