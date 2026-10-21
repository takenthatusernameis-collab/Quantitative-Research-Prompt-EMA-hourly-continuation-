# EMA Hourly Continuation — CTSI/USDT P50_144

**Symbol:** CTSI/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.7312 |
| net_win_rate | 0.4829 |
| gross_profit_factor | 0.9389 |
| gross_win_rate | 0.4829 |
| sharpe_ratio | -2.0766 |
| sortino_ratio | -0.6004 |
| max_drawdown | 0.5473 |
| cagr | -0.2411 |
| net_avg_win | 68.6817 |
| net_avg_loss | -87.7263 |
| avg_hold_time_bars | 16.5634 |
| exposure | 0.3087 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
