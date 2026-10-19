# EMA Hourly Continuation — RAY/USDT P20_26

**Symbol:** RAY/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1165 |
| net_profit_factor | 0.3267 |
| net_win_rate | 0.3828 |
| gross_profit_factor | 0.8130 |
| gross_win_rate | 0.4206 |
| sharpe_ratio | -12.4228 |
| sortino_ratio | -6.0848 |
| max_drawdown | 0.9996 |
| cagr | -0.9570 |
| net_avg_win | 10.8756 |
| net_avg_loss | -20.6492 |
| avg_hold_time_bars | 2.1030 |
| exposure | 0.1114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
