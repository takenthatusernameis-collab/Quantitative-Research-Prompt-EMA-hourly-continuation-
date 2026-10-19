# EMA Hourly Continuation — TRAC/USDT P12_144

**Symbol:** TRAC/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 555 |
| net_profit_factor | 0.6928 |
| net_win_rate | 0.4739 |
| gross_profit_factor | 0.9729 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -3.1242 |
| sortino_ratio | -1.0279 |
| max_drawdown | 0.7206 |
| cagr | -0.3919 |
| net_avg_win | 61.1504 |
| net_avg_loss | -79.5032 |
| avg_hold_time_bars | 23.5207 |
| exposure | 0.5934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
