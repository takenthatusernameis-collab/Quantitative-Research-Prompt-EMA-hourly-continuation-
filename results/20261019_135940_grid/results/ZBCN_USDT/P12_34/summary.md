# EMA Hourly Continuation — ZBCN/USDT P12_34

**Symbol:** ZBCN/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1400 |
| net_profit_factor | 0.5103 |
| net_win_rate | 0.4700 |
| gross_profit_factor | 0.8561 |
| gross_win_rate | 0.4743 |
| sharpe_ratio | -7.2342 |
| sortino_ratio | -3.8192 |
| max_drawdown | 0.9911 |
| cagr | -0.8495 |
| net_avg_win | 15.6898 |
| net_avg_loss | -27.2646 |
| avg_hold_time_bars | 3.6100 |
| exposure | 0.2338 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
