# EMA Hourly Continuation — ANKR/USDT P55_89

**Symbol:** ANKR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 677 |
| net_profit_factor | 0.3706 |
| net_win_rate | 0.3929 |
| gross_profit_factor | 0.7276 |
| gross_win_rate | 0.4210 |
| sharpe_ratio | -8.2406 |
| sortino_ratio | -3.0590 |
| max_drawdown | 0.9776 |
| cagr | -0.7787 |
| net_avg_win | 21.6367 |
| net_avg_loss | -37.7833 |
| avg_hold_time_bars | 6.1182 |
| exposure | 0.1883 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
