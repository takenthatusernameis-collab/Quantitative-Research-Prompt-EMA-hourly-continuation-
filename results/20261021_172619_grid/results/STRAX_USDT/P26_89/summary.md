# EMA Hourly Continuation — STRAX/USDT P26_89

**Symbol:** STRAX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 531 |
| net_profit_factor | 0.6342 |
| net_win_rate | 0.4520 |
| gross_profit_factor | 0.8625 |
| gross_win_rate | 0.4539 |
| sharpe_ratio | -3.7139 |
| sortino_ratio | -1.2167 |
| max_drawdown | 0.7658 |
| cagr | -0.4310 |
| net_avg_win | 54.5661 |
| net_avg_loss | -70.9592 |
| avg_hold_time_bars | 12.4162 |
| exposure | 0.3014 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
