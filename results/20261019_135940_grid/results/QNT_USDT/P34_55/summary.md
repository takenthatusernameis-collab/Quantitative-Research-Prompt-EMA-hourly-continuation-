# EMA Hourly Continuation — QNT/USDT P34_55

**Symbol:** QNT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 987 |
| net_profit_factor | 0.3083 |
| net_win_rate | 0.4174 |
| gross_profit_factor | 0.8073 |
| gross_win_rate | 0.4549 |
| sharpe_ratio | -10.1565 |
| sortino_ratio | -4.5601 |
| max_drawdown | 0.9968 |
| cagr | -0.8981 |
| net_avg_win | 10.7847 |
| net_avg_loss | -25.0625 |
| avg_hold_time_bars | 2.7720 |
| exposure | 0.1244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
