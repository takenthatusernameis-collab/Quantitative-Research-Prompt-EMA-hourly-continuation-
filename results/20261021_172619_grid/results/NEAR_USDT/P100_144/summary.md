# EMA Hourly Continuation — NEAR/USDT P100_144

**Symbol:** NEAR/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 208 |
| net_profit_factor | 0.8439 |
| net_win_rate | 0.5288 |
| gross_profit_factor | 1.0942 |
| gross_win_rate | 0.5288 |
| sharpe_ratio | -0.6542 |
| sortino_ratio | -0.1363 |
| max_drawdown | 0.2573 |
| cagr | -0.0617 |
| net_avg_win | 72.6714 |
| net_avg_loss | -96.6618 |
| avg_hold_time_bars | 5.7981 |
| exposure | 0.0548 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
