# EMA Hourly Continuation — XEC/USDT P12_26

**Symbol:** XEC/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.5849 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.9210 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -4.3573 |
| sortino_ratio | -1.6016 |
| max_drawdown | 0.8473 |
| cagr | -0.5183 |
| net_avg_win | 37.8835 |
| net_avg_loss | -58.9357 |
| avg_hold_time_bars | 5.4901 |
| exposure | 0.1632 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
