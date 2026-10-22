# EMA Hourly Continuation — BAT/USDT P8_20

**Symbol:** BAT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1577 |
| net_profit_factor | 0.2508 |
| net_win_rate | 0.4147 |
| gross_profit_factor | 0.6981 |
| gross_win_rate | 0.4490 |
| sharpe_ratio | -12.5559 |
| sortino_ratio | -7.0658 |
| max_drawdown | 0.9999 |
| cagr | -0.9718 |
| net_avg_win | 5.1182 |
| net_avg_loss | -14.4594 |
| avg_hold_time_bars | 3.2936 |
| exposure | 0.2361 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
