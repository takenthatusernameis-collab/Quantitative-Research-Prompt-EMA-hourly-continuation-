# EMA Hourly Continuation — FLR/USDT P20_200

**Symbol:** FLR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.6249 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 0.9603 |
| gross_win_rate | 0.4917 |
| sharpe_ratio | -3.4323 |
| sortino_ratio | -1.1304 |
| max_drawdown | 0.7536 |
| cagr | -0.4165 |
| net_avg_win | 46.7951 |
| net_avg_loss | -70.3532 |
| avg_hold_time_bars | 23.3138 |
| exposure | 0.5775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
