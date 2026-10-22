# EMA Hourly Continuation — BNB/USDT P8_55

**Symbol:** BNB/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1019 |
| net_profit_factor | 0.3424 |
| net_win_rate | 0.4377 |
| gross_profit_factor | 0.8900 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -9.5109 |
| sortino_ratio | -4.2780 |
| max_drawdown | 0.9961 |
| cagr | -0.8896 |
| net_avg_win | 11.6283 |
| net_avg_loss | -26.4340 |
| avg_hold_time_bars | 10.6546 |
| exposure | 0.4935 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
