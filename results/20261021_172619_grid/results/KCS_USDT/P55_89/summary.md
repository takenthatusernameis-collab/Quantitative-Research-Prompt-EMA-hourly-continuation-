# EMA Hourly Continuation — KCS/USDT P55_89

**Symbol:** KCS/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.4109 |
| net_win_rate | 0.4467 |
| gross_profit_factor | 0.8282 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -4.2950 |
| sortino_ratio | -1.0637 |
| max_drawdown | 0.7086 |
| cagr | -0.3836 |
| net_avg_win | 37.7452 |
| net_avg_loss | -74.1656 |
| avg_hold_time_bars | 7.5911 |
| exposure | 0.1004 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
