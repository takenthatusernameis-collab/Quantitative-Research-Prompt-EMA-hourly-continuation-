# EMA Hourly Continuation — MTL/USDT P89_100

**Symbol:** MTL/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 555 |
| net_profit_factor | 0.2397 |
| net_win_rate | 0.3423 |
| gross_profit_factor | 0.6338 |
| gross_win_rate | 0.4126 |
| sharpe_ratio | -9.6803 |
| sortino_ratio | -3.3055 |
| max_drawdown | 0.9877 |
| cagr | -0.8245 |
| net_avg_win | 16.3837 |
| net_avg_loss | -35.5860 |
| avg_hold_time_bars | 4.3045 |
| exposure | 0.1081 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
