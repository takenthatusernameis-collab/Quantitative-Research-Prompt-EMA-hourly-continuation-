# EMA Hourly Continuation — NOT/USDT P26_55

**Symbol:** NOT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.8329 |
| net_win_rate | 0.5188 |
| gross_profit_factor | 1.0716 |
| gross_win_rate | 0.5188 |
| sharpe_ratio | -1.1591 |
| sortino_ratio | -0.3389 |
| max_drawdown | 0.3657 |
| cagr | -0.1456 |
| net_avg_win | 76.5071 |
| net_avg_loss | -99.0351 |
| avg_hold_time_bars | 6.6015 |
| exposure | 0.1237 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
