# EMA Hourly Continuation — WEMIX/USDT P21_50

**Symbol:** WEMIX/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.5584 |
| net_win_rate | 0.4227 |
| gross_profit_factor | 0.7466 |
| gross_win_rate | 0.4227 |
| sharpe_ratio | -3.6501 |
| sortino_ratio | -0.9844 |
| max_drawdown | 0.6871 |
| cagr | -0.3660 |
| net_avg_win | 56.3341 |
| net_avg_loss | -73.8531 |
| avg_hold_time_bars | 11.5000 |
| exposure | 0.1892 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
