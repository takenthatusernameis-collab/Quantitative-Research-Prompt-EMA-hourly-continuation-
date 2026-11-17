# EMA Hourly Continuation — GMEE/USDT P34_144

**Symbol:** GMEE/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.5614 |
| net_win_rate | 0.4320 |
| gross_profit_factor | 0.7772 |
| gross_win_rate | 0.4386 |
| sharpe_ratio | -3.9327 |
| sortino_ratio | -1.1745 |
| max_drawdown | 0.7746 |
| cagr | -0.4323 |
| net_avg_win | 49.3047 |
| net_avg_loss | -66.7960 |
| avg_hold_time_bars | 20.2588 |
| exposure | 0.4199 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
