# EMA Hourly Continuation — FIL/USDT P50_100

**Symbol:** FIL/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.4295 |
| net_win_rate | 0.4313 |
| gross_profit_factor | 0.8065 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -6.1581 |
| sortino_ratio | -2.1695 |
| max_drawdown | 0.9353 |
| cagr | -0.6565 |
| net_avg_win | 25.9810 |
| net_avg_loss | -45.8758 |
| avg_hold_time_bars | 5.5447 |
| exposure | 0.1578 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
