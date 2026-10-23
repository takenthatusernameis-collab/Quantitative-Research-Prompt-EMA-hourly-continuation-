# EMA Hourly Continuation — CYBER/USDT P8_12

**Symbol:** CYBER/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1725 |
| net_profit_factor | 0.2528 |
| net_win_rate | 0.3948 |
| gross_profit_factor | 0.7301 |
| gross_win_rate | 0.4475 |
| sharpe_ratio | -15.7779 |
| sortino_ratio | -9.4314 |
| max_drawdown | 1.0000 |
| cagr | -0.9929 |
| net_avg_win | 4.9677 |
| net_avg_loss | -12.8189 |
| avg_hold_time_bars | 2.3571 |
| exposure | 0.1848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
