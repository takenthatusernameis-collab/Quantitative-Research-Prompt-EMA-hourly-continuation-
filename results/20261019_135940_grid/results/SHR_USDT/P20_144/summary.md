# EMA Hourly Continuation — SHR/USDT P20_144

**Symbol:** SHR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 838 |
| net_profit_factor | 0.4177 |
| net_win_rate | 0.3341 |
| gross_profit_factor | 0.5512 |
| gross_win_rate | 0.3341 |
| sharpe_ratio | -8.2577 |
| sortino_ratio | -3.3253 |
| max_drawdown | 0.9819 |
| cagr | -0.7953 |
| net_avg_win | 25.1475 |
| net_avg_loss | -30.2120 |
| avg_hold_time_bars | 11.6348 |
| exposure | 0.4412 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
