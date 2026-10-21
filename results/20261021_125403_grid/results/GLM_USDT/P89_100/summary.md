# EMA Hourly Continuation — GLM/USDT P89_100

**Symbol:** GLM/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 189 |
| net_profit_factor | 0.7218 |
| net_win_rate | 0.5503 |
| gross_profit_factor | 1.2140 |
| gross_win_rate | 0.5503 |
| sharpe_ratio | -1.3768 |
| sortino_ratio | -0.2731 |
| max_drawdown | 0.3231 |
| cagr | -0.1178 |
| net_avg_win | 67.3875 |
| net_avg_loss | -114.2288 |
| avg_hold_time_bars | 6.0794 |
| exposure | 0.0522 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
