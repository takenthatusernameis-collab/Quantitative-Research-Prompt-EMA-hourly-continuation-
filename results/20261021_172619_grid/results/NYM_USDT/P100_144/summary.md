# EMA Hourly Continuation — NYM/USDT P100_144

**Symbol:** NYM/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 186 |
| net_profit_factor | 0.3775 |
| net_win_rate | 0.3871 |
| gross_profit_factor | 0.6384 |
| gross_win_rate | 0.3871 |
| sharpe_ratio | -3.8970 |
| sortino_ratio | -0.7617 |
| max_drawdown | 0.5929 |
| cagr | -0.3008 |
| net_avg_win | 49.9349 |
| net_avg_loss | -83.5452 |
| avg_hold_time_bars | 11.4409 |
| exposure | 0.0967 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
