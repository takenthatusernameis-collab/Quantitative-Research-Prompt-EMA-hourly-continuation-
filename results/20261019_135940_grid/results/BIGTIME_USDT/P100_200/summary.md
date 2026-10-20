# EMA Hourly Continuation — BIGTIME/USDT P100_200

**Symbol:** BIGTIME/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.6679 |
| net_win_rate | 0.4822 |
| gross_profit_factor | 0.9521 |
| gross_win_rate | 0.4849 |
| sharpe_ratio | -2.5387 |
| sortino_ratio | -0.6855 |
| max_drawdown | 0.5602 |
| cagr | -0.2741 |
| net_avg_win | 63.3265 |
| net_avg_loss | -88.2965 |
| avg_hold_time_bars | 10.2658 |
| exposure | 0.1696 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
