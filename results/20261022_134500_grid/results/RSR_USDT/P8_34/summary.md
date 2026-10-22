# EMA Hourly Continuation — RSR/USDT P8_34

**Symbol:** RSR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1350 |
| net_profit_factor | 0.5495 |
| net_win_rate | 0.4541 |
| gross_profit_factor | 0.8985 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -7.2996 |
| sortino_ratio | -3.7642 |
| max_drawdown | 0.9900 |
| cagr | -0.8389 |
| net_avg_win | 19.6951 |
| net_avg_loss | -29.8115 |
| avg_hold_time_bars | 5.7489 |
| exposure | 0.3528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
