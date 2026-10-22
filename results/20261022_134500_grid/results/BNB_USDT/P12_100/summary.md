# EMA Hourly Continuation — BNB/USDT P12_100

**Symbol:** BNB/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.3356 |
| net_win_rate | 0.4144 |
| gross_profit_factor | 0.8336 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -7.9133 |
| sortino_ratio | -2.8888 |
| max_drawdown | 0.9765 |
| cagr | -0.7726 |
| net_avg_win | 17.8616 |
| net_avg_loss | -37.6598 |
| avg_hold_time_bars | 19.2688 |
| exposure | 0.5833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
