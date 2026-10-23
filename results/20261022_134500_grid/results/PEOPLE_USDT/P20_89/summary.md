# EMA Hourly Continuation — PEOPLE/USDT P20_89

**Symbol:** PEOPLE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 616 |
| net_profit_factor | 0.6135 |
| net_win_rate | 0.4562 |
| gross_profit_factor | 0.8569 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -3.9212 |
| sortino_ratio | -1.3640 |
| max_drawdown | 0.8204 |
| cagr | -0.4781 |
| net_avg_win | 45.5450 |
| net_avg_loss | -62.2668 |
| avg_hold_time_bars | 15.5828 |
| exposure | 0.4344 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
