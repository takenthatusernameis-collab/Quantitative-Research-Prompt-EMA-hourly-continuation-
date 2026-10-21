# EMA Hourly Continuation — JTO/USDT P50_144

**Symbol:** JTO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.6230 |
| net_win_rate | 0.4261 |
| gross_profit_factor | 0.7487 |
| gross_win_rate | 0.4261 |
| sharpe_ratio | -2.7537 |
| sortino_ratio | -0.7216 |
| max_drawdown | 0.5930 |
| cagr | -0.2826 |
| net_avg_win | 63.6050 |
| net_avg_loss | -75.7967 |
| avg_hold_time_bars | 16.1130 |
| exposure | 0.2527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
