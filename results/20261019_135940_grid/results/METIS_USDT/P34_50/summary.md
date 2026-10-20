# EMA Hourly Continuation — METIS/USDT P34_50

**Symbol:** METIS/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 924 |
| net_profit_factor | 0.3588 |
| net_win_rate | 0.4188 |
| gross_profit_factor | 0.7740 |
| gross_win_rate | 0.4416 |
| sharpe_ratio | -9.2652 |
| sortino_ratio | -4.0093 |
| max_drawdown | 0.9940 |
| cagr | -0.8683 |
| net_avg_win | 14.3728 |
| net_avg_loss | -28.8655 |
| avg_hold_time_bars | 2.9188 |
| exposure | 0.1226 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
