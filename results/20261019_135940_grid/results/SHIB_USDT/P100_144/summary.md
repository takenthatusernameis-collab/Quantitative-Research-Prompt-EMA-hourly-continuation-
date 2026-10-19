# EMA Hourly Continuation — SHIB/USDT P100_144

**Symbol:** SHIB/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 522 |
| net_profit_factor | 0.3977 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.8684 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -6.2516 |
| sortino_ratio | -2.0269 |
| max_drawdown | 0.9243 |
| cagr | -0.6391 |
| net_avg_win | 25.7030 |
| net_avg_loss | -53.7486 |
| avg_hold_time_bars | 3.7701 |
| exposure | 0.0895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
