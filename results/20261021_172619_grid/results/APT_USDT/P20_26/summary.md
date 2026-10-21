# EMA Hourly Continuation — APT/USDT P20_26

**Symbol:** APT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 164 |
| net_profit_factor | 0.6361 |
| net_win_rate | 0.4756 |
| gross_profit_factor | 0.8950 |
| gross_win_rate | 0.4756 |
| sharpe_ratio | -1.7513 |
| sortino_ratio | -0.3212 |
| max_drawdown | 0.3253 |
| cagr | -0.1363 |
| net_avg_win | 68.9966 |
| net_avg_loss | -98.3828 |
| avg_hold_time_bars | 4.9878 |
| exposure | 0.0372 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
