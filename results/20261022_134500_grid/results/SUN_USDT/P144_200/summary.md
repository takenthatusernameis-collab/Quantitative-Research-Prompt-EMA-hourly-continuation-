# EMA Hourly Continuation — SUN/USDT P144_200

**Symbol:** SUN/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.2472 |
| net_win_rate | 0.3558 |
| gross_profit_factor | 0.7041 |
| gross_win_rate | 0.4234 |
| sharpe_ratio | -8.0320 |
| sortino_ratio | -2.2967 |
| max_drawdown | 0.9544 |
| cagr | -0.7042 |
| net_avg_win | 22.8626 |
| net_avg_loss | -51.0860 |
| avg_hold_time_bars | 6.1013 |
| exposure | 0.1063 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
