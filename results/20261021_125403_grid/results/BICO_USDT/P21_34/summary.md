# EMA Hourly Continuation — BICO/USDT P21_34

**Symbol:** BICO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.6113 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.8774 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -3.3328 |
| sortino_ratio | -1.0503 |
| max_drawdown | 0.7024 |
| cagr | -0.3809 |
| net_avg_win | 48.2876 |
| net_avg_loss | -69.8087 |
| avg_hold_time_bars | 5.0597 |
| exposure | 0.1118 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
