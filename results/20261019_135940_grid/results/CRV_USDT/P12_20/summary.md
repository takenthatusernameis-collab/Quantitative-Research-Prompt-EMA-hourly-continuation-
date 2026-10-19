# EMA Hourly Continuation — CRV/USDT P12_20

**Symbol:** CRV/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1488 |
| net_profit_factor | 0.2984 |
| net_win_rate | 0.4301 |
| gross_profit_factor | 0.7447 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -11.9533 |
| sortino_ratio | -6.5517 |
| max_drawdown | 0.9998 |
| cagr | -0.9646 |
| net_avg_win | 6.6455 |
| net_avg_loss | -16.8052 |
| avg_hold_time_bars | 2.0585 |
| exposure | 0.1392 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
