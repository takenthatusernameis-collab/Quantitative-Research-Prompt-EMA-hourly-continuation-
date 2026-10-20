# EMA Hourly Continuation — KSM/USDT P8_12

**Symbol:** KSM/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1855 |
| net_profit_factor | 0.1651 |
| net_win_rate | 0.3585 |
| gross_profit_factor | 0.6659 |
| gross_win_rate | 0.4194 |
| sharpe_ratio | -18.3608 |
| sortino_ratio | -11.4927 |
| max_drawdown | 1.0000 |
| cagr | -0.9977 |
| net_avg_win | 2.9731 |
| net_avg_loss | -10.0648 |
| avg_hold_time_bars | 1.9919 |
| exposure | 0.1680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
