# EMA Hourly Continuation — LPT/USDT P12_21

**Symbol:** LPT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.6257 |
| net_win_rate | 0.4716 |
| gross_profit_factor | 0.9042 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -3.5102 |
| sortino_ratio | -1.0754 |
| max_drawdown | 0.7154 |
| cagr | -0.3908 |
| net_avg_win | 55.0976 |
| net_avg_loss | -78.5953 |
| avg_hold_time_bars | 4.8624 |
| exposure | 0.1012 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
