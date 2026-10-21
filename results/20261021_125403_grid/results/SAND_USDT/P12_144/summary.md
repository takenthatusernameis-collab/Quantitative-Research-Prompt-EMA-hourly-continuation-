# EMA Hourly Continuation — SAND/USDT P12_144

**Symbol:** SAND/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.7879 |
| net_win_rate | 0.4901 |
| gross_profit_factor | 0.9661 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -1.3302 |
| sortino_ratio | -0.3312 |
| max_drawdown | 0.3322 |
| cagr | -0.1423 |
| net_avg_win | 79.7702 |
| net_avg_loss | -97.3230 |
| avg_hold_time_bars | 51.7533 |
| exposure | 0.7151 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
