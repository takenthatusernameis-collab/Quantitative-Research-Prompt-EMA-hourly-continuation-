# EMA Hourly Continuation — CFG/USDT P21_55

**Symbol:** CFG/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.6684 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.8530 |
| gross_win_rate | 0.4637 |
| sharpe_ratio | -2.2669 |
| sortino_ratio | -0.6100 |
| max_drawdown | 0.5283 |
| cagr | -0.2446 |
| net_avg_win | 61.3957 |
| net_avg_loss | -79.4181 |
| avg_hold_time_bars | 23.6285 |
| exposure | 0.3845 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
