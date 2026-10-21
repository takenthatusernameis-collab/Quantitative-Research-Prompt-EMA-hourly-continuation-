# EMA Hourly Continuation — BTC/USDT P89_200

**Symbol:** BTC/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.8105 |
| net_win_rate | 0.5674 |
| gross_profit_factor | 1.3264 |
| gross_win_rate | 0.5709 |
| sharpe_ratio | -1.0116 |
| sortino_ratio | -0.2316 |
| max_drawdown | 0.3603 |
| cagr | -0.1005 |
| net_avg_win | 69.7504 |
| net_avg_loss | -112.8667 |
| avg_hold_time_bars | 15.0957 |
| exposure | 0.1703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
