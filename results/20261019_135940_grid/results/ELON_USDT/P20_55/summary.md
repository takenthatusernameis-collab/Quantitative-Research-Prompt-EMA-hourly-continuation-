# EMA Hourly Continuation — ELON/USDT P20_55

**Symbol:** ELON/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 939 |
| net_profit_factor | 0.4003 |
| net_win_rate | 0.4175 |
| gross_profit_factor | 0.7208 |
| gross_win_rate | 0.4228 |
| sharpe_ratio | -8.3719 |
| sortino_ratio | -3.6441 |
| max_drawdown | 0.9882 |
| cagr | -0.8287 |
| net_avg_win | 16.8272 |
| net_avg_loss | -30.1229 |
| avg_hold_time_bars | 5.2545 |
| exposure | 0.2243 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
