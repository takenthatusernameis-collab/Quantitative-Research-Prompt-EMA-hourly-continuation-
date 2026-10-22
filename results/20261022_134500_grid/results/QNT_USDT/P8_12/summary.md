# EMA Hourly Continuation — QNT/USDT P8_12

**Symbol:** QNT/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1848 |
| net_profit_factor | 0.1648 |
| net_win_rate | 0.3285 |
| gross_profit_factor | 0.7546 |
| gross_win_rate | 0.4102 |
| sharpe_ratio | -20.1467 |
| sortino_ratio | -12.8034 |
| max_drawdown | 1.0000 |
| cagr | -0.9991 |
| net_avg_win | 3.2512 |
| net_avg_loss | -9.6483 |
| avg_hold_time_bars | 1.8371 |
| exposure | 0.1543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
