# EMA Hourly Continuation — ZETA/USDT P34_100

**Symbol:** ZETA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.7636 |
| net_win_rate | 0.4850 |
| gross_profit_factor | 0.9683 |
| gross_win_rate | 0.4850 |
| sharpe_ratio | -2.0624 |
| sortino_ratio | -0.6358 |
| max_drawdown | 0.5811 |
| cagr | -0.2538 |
| net_avg_win | 74.3092 |
| net_avg_loss | -91.6609 |
| avg_hold_time_bars | 12.1218 |
| exposure | 0.2567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
