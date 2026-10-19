# EMA Hourly Continuation — NEAR/USDT P20_26

**Symbol:** NEAR/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1217 |
| net_profit_factor | 0.2560 |
| net_win_rate | 0.3689 |
| gross_profit_factor | 0.7015 |
| gross_win_rate | 0.3903 |
| sharpe_ratio | -14.2449 |
| sortino_ratio | -7.1894 |
| max_drawdown | 0.9999 |
| cagr | -0.9788 |
| net_avg_win | 7.6647 |
| net_avg_loss | -17.5011 |
| avg_hold_time_bars | 1.8102 |
| exposure | 0.1001 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
