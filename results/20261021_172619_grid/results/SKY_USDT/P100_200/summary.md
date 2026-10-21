# EMA Hourly Continuation — SKY/USDT P100_200

**Symbol:** SKY/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.9537 |
| net_win_rate | 0.5605 |
| gross_profit_factor | 1.2630 |
| gross_win_rate | 0.5605 |
| sharpe_ratio | -0.2253 |
| sortino_ratio | -0.0571 |
| max_drawdown | 0.2595 |
| cagr | -0.0303 |
| net_avg_win | 90.3963 |
| net_avg_loss | -120.8674 |
| avg_hold_time_bars | 10.4798 |
| exposure | 0.1449 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
