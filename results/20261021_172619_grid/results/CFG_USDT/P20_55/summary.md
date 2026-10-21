# EMA Hourly Continuation — CFG/USDT P20_55

**Symbol:** CFG/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.6303 |
| net_win_rate | 0.4488 |
| gross_profit_factor | 0.8044 |
| gross_win_rate | 0.4488 |
| sharpe_ratio | -2.6898 |
| sortino_ratio | -0.7447 |
| max_drawdown | 0.5967 |
| cagr | -0.2903 |
| net_avg_win | 57.5504 |
| net_avg_loss | -74.3532 |
| avg_hold_time_bars | 22.7743 |
| exposure | 0.3944 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
