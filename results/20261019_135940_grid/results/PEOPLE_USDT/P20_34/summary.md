# EMA Hourly Continuation — PEOPLE/USDT P20_34

**Symbol:** PEOPLE/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1114 |
| net_profit_factor | 0.4032 |
| net_win_rate | 0.4210 |
| gross_profit_factor | 0.7355 |
| gross_win_rate | 0.4425 |
| sharpe_ratio | -9.1062 |
| sortino_ratio | -4.2928 |
| max_drawdown | 0.9950 |
| cagr | -0.8779 |
| net_avg_win | 14.3352 |
| net_avg_loss | -25.8504 |
| avg_hold_time_bars | 2.9246 |
| exposure | 0.1474 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
