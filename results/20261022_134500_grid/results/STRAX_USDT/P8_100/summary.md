# EMA Hourly Continuation — STRAX/USDT P8_100

**Symbol:** STRAX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 812 |
| net_profit_factor | 0.6056 |
| net_win_rate | 0.4323 |
| gross_profit_factor | 0.8944 |
| gross_win_rate | 0.4433 |
| sharpe_ratio | -6.0588 |
| sortino_ratio | -2.4319 |
| max_drawdown | 0.9467 |
| cagr | -0.6909 |
| net_avg_win | 41.4226 |
| net_avg_loss | -52.0742 |
| avg_hold_time_bars | 16.5603 |
| exposure | 0.6148 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
