# EMA Hourly Continuation — CAKE/USDT P21_89

**Symbol:** CAKE/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.8237 |
| net_win_rate | 0.5196 |
| gross_profit_factor | 1.0912 |
| gross_win_rate | 0.5216 |
| sharpe_ratio | -1.3861 |
| sortino_ratio | -0.4387 |
| max_drawdown | 0.4464 |
| cagr | -0.1843 |
| net_avg_win | 74.2412 |
| net_avg_loss | -97.4792 |
| avg_hold_time_bars | 16.5588 |
| exposure | 0.3650 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
