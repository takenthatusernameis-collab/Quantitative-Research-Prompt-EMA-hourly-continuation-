# EMA Hourly Continuation — NOT/USDT P55_200

**Symbol:** NOT/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.6237 |
| net_win_rate | 0.4709 |
| gross_profit_factor | 0.8754 |
| gross_win_rate | 0.4734 |
| sharpe_ratio | -2.8395 |
| sortino_ratio | -0.8015 |
| max_drawdown | 0.6122 |
| cagr | -0.3205 |
| net_avg_win | 54.2691 |
| net_avg_loss | -77.4355 |
| avg_hold_time_bars | 18.6506 |
| exposure | 0.3461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
