# EMA Hourly Continuation — DEEP/USDT P34_55

**Symbol:** DEEP/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.8667 |
| net_win_rate | 0.5286 |
| gross_profit_factor | 1.1121 |
| gross_win_rate | 0.5286 |
| sharpe_ratio | -0.7329 |
| sortino_ratio | -0.1777 |
| max_drawdown | 0.2389 |
| cagr | -0.0804 |
| net_avg_win | 84.3133 |
| net_avg_loss | -109.0952 |
| avg_hold_time_bars | 6.4846 |
| exposure | 0.0833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
