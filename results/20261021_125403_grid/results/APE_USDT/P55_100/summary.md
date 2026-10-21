# EMA Hourly Continuation — APE/USDT P55_100

**Symbol:** APE/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.6518 |
| net_win_rate | 0.4626 |
| gross_profit_factor | 0.8575 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -2.5013 |
| sortino_ratio | -0.6651 |
| max_drawdown | 0.5495 |
| cagr | -0.2627 |
| net_avg_win | 62.1826 |
| net_avg_loss | -82.1336 |
| avg_hold_time_bars | 7.9282 |
| exposure | 0.1254 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
