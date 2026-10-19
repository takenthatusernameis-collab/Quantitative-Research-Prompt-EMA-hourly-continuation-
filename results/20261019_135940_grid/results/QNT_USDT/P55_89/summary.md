# EMA Hourly Continuation — QNT/USDT P55_89

**Symbol:** QNT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 777 |
| net_profit_factor | 0.3423 |
| net_win_rate | 0.4015 |
| gross_profit_factor | 0.7040 |
| gross_win_rate | 0.4157 |
| sharpe_ratio | -8.9638 |
| sortino_ratio | -3.5468 |
| max_drawdown | 0.9895 |
| cagr | -0.8336 |
| net_avg_win | 16.4940 |
| net_avg_loss | -32.3343 |
| avg_hold_time_bars | 3.7130 |
| exposure | 0.1311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
