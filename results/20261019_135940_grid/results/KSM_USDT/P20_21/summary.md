# EMA Hourly Continuation — KSM/USDT P20_21

**Symbol:** KSM/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1237 |
| net_profit_factor | 0.1386 |
| net_win_rate | 0.2926 |
| gross_profit_factor | 0.6897 |
| gross_win_rate | 0.3969 |
| sharpe_ratio | -18.2176 |
| sortino_ratio | -9.7838 |
| max_drawdown | 1.0000 |
| cagr | -0.9959 |
| net_avg_win | 4.4436 |
| net_avg_loss | -13.2670 |
| avg_hold_time_bars | 1.7146 |
| exposure | 0.0964 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
