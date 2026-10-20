# EMA Hourly Continuation — SNX/USDT P20_26

**Symbol:** SNX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1187 |
| net_profit_factor | 0.2667 |
| net_win_rate | 0.3960 |
| gross_profit_factor | 0.8094 |
| gross_win_rate | 0.4465 |
| sharpe_ratio | -12.6062 |
| sortino_ratio | -6.2342 |
| max_drawdown | 0.9997 |
| cagr | -0.9609 |
| net_avg_win | 7.7346 |
| net_avg_loss | -19.0132 |
| avg_hold_time_bars | 1.9815 |
| exposure | 0.1064 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
