# EMA Hourly Continuation — CAKE/USDT P8_200

**Symbol:** CAKE/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.6172 |
| net_win_rate | 0.4744 |
| gross_profit_factor | 0.9801 |
| gross_win_rate | 0.4953 |
| sharpe_ratio | -3.3186 |
| sortino_ratio | -0.9515 |
| max_drawdown | 0.7216 |
| cagr | -0.3777 |
| net_avg_win | 55.0137 |
| net_avg_loss | -80.4601 |
| avg_hold_time_bars | 39.3070 |
| exposure | 0.7683 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
