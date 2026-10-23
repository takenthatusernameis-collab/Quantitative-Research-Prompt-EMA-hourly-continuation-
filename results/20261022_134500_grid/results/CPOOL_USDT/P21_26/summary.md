# EMA Hourly Continuation — CPOOL/USDT P21_26

**Symbol:** CPOOL/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1129 |
| net_profit_factor | 0.3595 |
| net_win_rate | 0.4012 |
| gross_profit_factor | 0.7594 |
| gross_win_rate | 0.4305 |
| sharpe_ratio | -11.4254 |
| sortino_ratio | -5.4219 |
| max_drawdown | 0.9993 |
| cagr | -0.9444 |
| net_avg_win | 12.3789 |
| net_avg_loss | -23.0778 |
| avg_hold_time_bars | 1.9566 |
| exposure | 0.1004 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
