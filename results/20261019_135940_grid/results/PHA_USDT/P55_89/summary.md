# EMA Hourly Continuation — PHA/USDT P55_89

**Symbol:** PHA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.4419 |
| net_win_rate | 0.4310 |
| gross_profit_factor | 0.7737 |
| gross_win_rate | 0.4367 |
| sharpe_ratio | -6.3912 |
| sortino_ratio | -2.3763 |
| max_drawdown | 0.9470 |
| cagr | -0.6896 |
| net_avg_win | 24.7494 |
| net_avg_loss | -42.4235 |
| avg_hold_time_bars | 3.9502 |
| exposure | 0.1262 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
