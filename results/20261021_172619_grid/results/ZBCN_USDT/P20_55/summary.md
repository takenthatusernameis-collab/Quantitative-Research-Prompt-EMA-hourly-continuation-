# EMA Hourly Continuation — ZBCN/USDT P20_55

**Symbol:** ZBCN/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.8902 |
| net_win_rate | 0.5206 |
| gross_profit_factor | 1.0791 |
| gross_win_rate | 0.5206 |
| sharpe_ratio | -0.7703 |
| sortino_ratio | -0.2401 |
| max_drawdown | 0.3439 |
| cagr | -0.1083 |
| net_avg_win | 83.2137 |
| net_avg_loss | -101.5166 |
| avg_hold_time_bars | 7.8243 |
| exposure | 0.1669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
