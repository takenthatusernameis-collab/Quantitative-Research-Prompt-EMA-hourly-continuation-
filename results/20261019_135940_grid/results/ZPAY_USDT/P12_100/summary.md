# EMA Hourly Continuation — ZPAY/USDT P12_100

**Symbol:** ZPAY/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.5011 |
| net_win_rate | 0.3607 |
| gross_profit_factor | 0.6268 |
| gross_win_rate | 0.3607 |
| sharpe_ratio | -5.0376 |
| sortino_ratio | -1.5089 |
| max_drawdown | 0.8421 |
| cagr | -0.5056 |
| net_avg_win | 49.9720 |
| net_avg_loss | -56.2625 |
| avg_hold_time_bars | 29.3002 |
| exposure | 0.6139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
