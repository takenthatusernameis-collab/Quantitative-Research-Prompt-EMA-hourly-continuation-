# EMA Hourly Continuation — ZPAY/USDT P21_26

**Symbol:** ZPAY/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 938 |
| net_profit_factor | 0.2790 |
| net_win_rate | 0.3134 |
| gross_profit_factor | 0.5999 |
| gross_win_rate | 0.3294 |
| sharpe_ratio | -11.4215 |
| sortino_ratio | -4.8947 |
| max_drawdown | 0.9979 |
| cagr | -0.9134 |
| net_avg_win | 13.1360 |
| net_avg_loss | -21.4923 |
| avg_hold_time_bars | 5.0842 |
| exposure | 0.2158 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
