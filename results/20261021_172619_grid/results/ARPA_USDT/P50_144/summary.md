# EMA Hourly Continuation — ARPA/USDT P50_144

**Symbol:** ARPA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.6023 |
| net_win_rate | 0.4539 |
| gross_profit_factor | 0.8036 |
| gross_win_rate | 0.4563 |
| sharpe_ratio | -3.0515 |
| sortino_ratio | -0.8908 |
| max_drawdown | 0.6524 |
| cagr | -0.3353 |
| net_avg_win | 50.7335 |
| net_avg_loss | -70.0079 |
| avg_hold_time_bars | 14.7163 |
| exposure | 0.2817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
