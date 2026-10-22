# EMA Hourly Continuation — BLZ/USDT P21_26

**Symbol:** BLZ/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1222 |
| net_profit_factor | 0.2113 |
| net_win_rate | 0.3273 |
| gross_profit_factor | 0.6880 |
| gross_win_rate | 0.3822 |
| sharpe_ratio | -15.4089 |
| sortino_ratio | -7.8149 |
| max_drawdown | 1.0000 |
| cagr | -0.9844 |
| net_avg_win | 6.6956 |
| net_avg_loss | -15.4233 |
| avg_hold_time_bars | 2.8167 |
| exposure | 0.1558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
