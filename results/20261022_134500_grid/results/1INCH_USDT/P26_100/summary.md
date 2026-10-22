# EMA Hourly Continuation — 1INCH/USDT P26_100

**Symbol:** 1INCH/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 687 |
| net_profit_factor | 0.5012 |
| net_win_rate | 0.4338 |
| gross_profit_factor | 0.8424 |
| gross_win_rate | 0.4527 |
| sharpe_ratio | -6.0416 |
| sortino_ratio | -2.2202 |
| max_drawdown | 0.9376 |
| cagr | -0.6649 |
| net_avg_win | 31.5535 |
| net_avg_loss | -48.2280 |
| avg_hold_time_bars | 12.1383 |
| exposure | 0.3790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
