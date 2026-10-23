# EMA Hourly Continuation — NOT/USDT P21_26

**Symbol:** NOT/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1205 |
| net_profit_factor | 0.3499 |
| net_win_rate | 0.3710 |
| gross_profit_factor | 0.7889 |
| gross_win_rate | 0.4033 |
| sharpe_ratio | -14.1156 |
| sortino_ratio | -7.2168 |
| max_drawdown | 0.9999 |
| cagr | -0.9784 |
| net_avg_win | 12.0373 |
| net_avg_loss | -20.2899 |
| avg_hold_time_bars | 1.8124 |
| exposure | 0.1026 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
