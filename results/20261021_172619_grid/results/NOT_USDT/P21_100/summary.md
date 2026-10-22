# EMA Hourly Continuation — NOT/USDT P21_100

**Symbol:** NOT/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.8338 |
| net_win_rate | 0.5059 |
| gross_profit_factor | 1.0036 |
| gross_win_rate | 0.5059 |
| sharpe_ratio | -1.0866 |
| sortino_ratio | -0.3274 |
| max_drawdown | 0.3415 |
| cagr | -0.1419 |
| net_avg_win | 72.1609 |
| net_avg_loss | -88.5933 |
| avg_hold_time_bars | 19.4473 |
| exposure | 0.3901 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
