# EMA Hourly Continuation — TAIKO/USDT P50_100

**Symbol:** TAIKO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 546 |
| net_profit_factor | 0.4821 |
| net_win_rate | 0.4414 |
| gross_profit_factor | 0.7830 |
| gross_win_rate | 0.4542 |
| sharpe_ratio | -5.4611 |
| sortino_ratio | -1.8492 |
| max_drawdown | 0.8895 |
| cagr | -0.5922 |
| net_avg_win | 34.0402 |
| net_avg_loss | -55.7938 |
| avg_hold_time_bars | 6.4780 |
| exposure | 0.1699 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
