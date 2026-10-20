# EMA Hourly Continuation — FLIP/USDT P21_34

**Symbol:** FLIP/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 801 |
| net_profit_factor | 0.2932 |
| net_win_rate | 0.3496 |
| gross_profit_factor | 0.7792 |
| gross_win_rate | 0.4182 |
| sharpe_ratio | -11.2560 |
| sortino_ratio | -4.5815 |
| max_drawdown | 0.9980 |
| cagr | -0.9153 |
| net_avg_win | 14.7820 |
| net_avg_loss | -27.0991 |
| avg_hold_time_bars | 5.1086 |
| exposure | 0.1860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
