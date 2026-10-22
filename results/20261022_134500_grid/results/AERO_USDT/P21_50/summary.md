# EMA Hourly Continuation — AERO/USDT P21_50

**Symbol:** AERO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 893 |
| net_profit_factor | 0.4967 |
| net_win_rate | 0.4681 |
| gross_profit_factor | 0.8433 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -5.8002 |
| sortino_ratio | -2.4238 |
| max_drawdown | 0.9512 |
| cagr | -0.6969 |
| net_avg_win | 22.4310 |
| net_avg_loss | -39.7417 |
| avg_hold_time_bars | 4.7032 |
| exposure | 0.1909 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
