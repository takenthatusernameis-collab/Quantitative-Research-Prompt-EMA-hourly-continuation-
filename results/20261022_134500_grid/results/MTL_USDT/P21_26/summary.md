# EMA Hourly Continuation — MTL/USDT P21_26

**Symbol:** MTL/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1123 |
| net_profit_factor | 0.2110 |
| net_win_rate | 0.3286 |
| gross_profit_factor | 0.7555 |
| gross_win_rate | 0.4052 |
| sharpe_ratio | -15.2302 |
| sortino_ratio | -7.4975 |
| max_drawdown | 1.0000 |
| cagr | -0.9815 |
| net_avg_win | 7.2466 |
| net_avg_loss | -16.8084 |
| avg_hold_time_bars | 2.8388 |
| exposure | 0.1443 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
