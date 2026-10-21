# EMA Hourly Continuation — BTC/USDT P12_100

**Symbol:** BTC/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.6703 |
| net_win_rate | 0.5083 |
| gross_profit_factor | 1.0028 |
| gross_win_rate | 0.5103 |
| sharpe_ratio | -2.3985 |
| sortino_ratio | -0.7113 |
| max_drawdown | 0.6105 |
| cagr | -0.2762 |
| net_avg_win | 49.7818 |
| net_avg_loss | -76.7676 |
| avg_hold_time_bars | 29.1405 |
| exposure | 0.5642 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
