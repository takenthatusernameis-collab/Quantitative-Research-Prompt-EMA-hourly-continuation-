# EMA Hourly Continuation — CFG/USDT P100_200

**Symbol:** CFG/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.5378 |
| net_win_rate | 0.4436 |
| gross_profit_factor | 0.7742 |
| gross_win_rate | 0.4484 |
| sharpe_ratio | -3.4741 |
| sortino_ratio | -0.9972 |
| max_drawdown | 0.7029 |
| cagr | -0.3768 |
| net_avg_win | 43.7161 |
| net_avg_loss | -64.8159 |
| avg_hold_time_bars | 8.7194 |
| exposure | 0.1653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
