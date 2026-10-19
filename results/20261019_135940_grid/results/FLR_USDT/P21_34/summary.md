# EMA Hourly Continuation — FLR/USDT P21_34

**Symbol:** FLR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1330 |
| net_profit_factor | 0.3303 |
| net_win_rate | 0.3534 |
| gross_profit_factor | 0.8396 |
| gross_win_rate | 0.3947 |
| sharpe_ratio | -14.9903 |
| sortino_ratio | -7.8997 |
| max_drawdown | 1.0000 |
| cagr | -0.9842 |
| net_avg_win | 10.4941 |
| net_avg_loss | -17.3627 |
| avg_hold_time_bars | 2.5195 |
| exposure | 0.1523 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
