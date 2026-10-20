# EMA Hourly Continuation — ONE/USDT P8_12

**Symbol:** ONE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1845 |
| net_profit_factor | 0.1728 |
| net_win_rate | 0.3615 |
| gross_profit_factor | 0.5759 |
| gross_win_rate | 0.3962 |
| sharpe_ratio | -17.5648 |
| sortino_ratio | -10.8280 |
| max_drawdown | 1.0000 |
| cagr | -0.9968 |
| net_avg_win | 3.1324 |
| net_avg_loss | -10.2626 |
| avg_hold_time_bars | 1.7079 |
| exposure | 0.1432 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
