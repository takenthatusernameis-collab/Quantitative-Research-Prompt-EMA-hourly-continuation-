# EMA Hourly Continuation — POKT/USDT P34_55

**Symbol:** POKT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 971 |
| net_profit_factor | 0.4258 |
| net_win_rate | 0.3913 |
| gross_profit_factor | 0.8899 |
| gross_win_rate | 0.4119 |
| sharpe_ratio | -9.7121 |
| sortino_ratio | -4.2719 |
| max_drawdown | 0.9955 |
| cagr | -0.8822 |
| net_avg_win | 19.4283 |
| net_avg_loss | -29.3357 |
| avg_hold_time_bars | 4.0360 |
| exposure | 0.1773 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
