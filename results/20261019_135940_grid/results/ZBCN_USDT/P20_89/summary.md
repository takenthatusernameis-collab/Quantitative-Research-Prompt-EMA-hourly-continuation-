# EMA Hourly Continuation — ZBCN/USDT P20_89

**Symbol:** ZBCN/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 887 |
| net_profit_factor | 0.6320 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9468 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -3.9157 |
| sortino_ratio | -1.6577 |
| max_drawdown | 0.8667 |
| cagr | -0.5474 |
| net_avg_win | 34.0585 |
| net_avg_loss | -51.3936 |
| avg_hold_time_bars | 7.9876 |
| exposure | 0.3278 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
