# EMA Hourly Continuation — EIGEN/USDT P8_89

**Symbol:** EIGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.8172 |
| net_win_rate | 0.4842 |
| gross_profit_factor | 0.9399 |
| gross_win_rate | 0.4842 |
| sharpe_ratio | -1.3851 |
| sortino_ratio | -0.4259 |
| max_drawdown | 0.3966 |
| cagr | -0.1800 |
| net_avg_win | 81.2633 |
| net_avg_loss | -93.3474 |
| avg_hold_time_bars | 30.0579 |
| exposure | 0.6356 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
