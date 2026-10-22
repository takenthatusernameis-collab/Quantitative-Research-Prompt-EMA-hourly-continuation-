# EMA Hourly Continuation — CAKE/USDT P12_26

**Symbol:** CAKE/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1347 |
| net_profit_factor | 0.3647 |
| net_win_rate | 0.4143 |
| gross_profit_factor | 1.0486 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -12.1998 |
| sortino_ratio | -6.3940 |
| max_drawdown | 0.9997 |
| cagr | -0.9622 |
| net_avg_win | 10.2852 |
| net_avg_loss | -19.9448 |
| avg_hold_time_bars | 3.1188 |
| exposure | 0.1910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
