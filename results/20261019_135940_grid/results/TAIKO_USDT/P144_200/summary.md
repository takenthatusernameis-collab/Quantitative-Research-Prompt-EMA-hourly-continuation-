# EMA Hourly Continuation — TAIKO/USDT P144_200

**Symbol:** TAIKO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.4946 |
| net_win_rate | 0.4343 |
| gross_profit_factor | 0.9010 |
| gross_win_rate | 0.4531 |
| sharpe_ratio | -5.2336 |
| sortino_ratio | -1.4626 |
| max_drawdown | 0.8358 |
| cagr | -0.5221 |
| net_avg_win | 49.9590 |
| net_avg_loss | -77.5517 |
| avg_hold_time_bars | 4.3190 |
| exposure | 0.0774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
