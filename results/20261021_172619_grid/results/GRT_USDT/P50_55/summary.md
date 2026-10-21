# EMA Hourly Continuation — GRT/USDT P50_55

**Symbol:** GRT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 92 |
| net_profit_factor | 0.8790 |
| net_win_rate | 0.5543 |
| gross_profit_factor | 1.2394 |
| gross_win_rate | 0.5543 |
| sharpe_ratio | -0.3762 |
| sortino_ratio | -0.0523 |
| max_drawdown | 0.1557 |
| cagr | -0.0243 |
| net_avg_win | 85.7871 |
| net_avg_loss | -121.4033 |
| avg_hold_time_bars | 5.8152 |
| exposure | 0.0242 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
