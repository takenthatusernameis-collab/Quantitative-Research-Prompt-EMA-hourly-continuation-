# EMA Hourly Continuation — ZBCN/USDT P12_100

**Symbol:** ZBCN/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 548 |
| net_profit_factor | 0.9295 |
| net_win_rate | 0.5219 |
| gross_profit_factor | 1.0799 |
| gross_win_rate | 0.5219 |
| sharpe_ratio | -0.4821 |
| sortino_ratio | -0.1638 |
| max_drawdown | 0.2588 |
| cagr | -0.0797 |
| net_avg_win | 85.3973 |
| net_avg_loss | -100.2944 |
| avg_hold_time_bars | 19.1588 |
| exposure | 0.4857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
