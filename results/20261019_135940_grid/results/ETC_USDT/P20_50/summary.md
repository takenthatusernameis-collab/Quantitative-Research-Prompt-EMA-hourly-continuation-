# EMA Hourly Continuation — ETC/USDT P20_50

**Symbol:** ETC/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1007 |
| net_profit_factor | 0.3701 |
| net_win_rate | 0.4240 |
| gross_profit_factor | 0.8385 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -9.7614 |
| sortino_ratio | -4.3868 |
| max_drawdown | 0.9964 |
| cagr | -0.8925 |
| net_avg_win | 13.7103 |
| net_avg_loss | -27.2713 |
| avg_hold_time_bars | 4.7507 |
| exposure | 0.2175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
