# EMA Hourly Continuation — SAND/USDT P12_50

**Symbol:** SAND/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 996 |
| net_profit_factor | 0.4949 |
| net_win_rate | 0.4378 |
| gross_profit_factor | 0.8825 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -7.4874 |
| sortino_ratio | -3.3051 |
| max_drawdown | 0.9846 |
| cagr | -0.8070 |
| net_avg_win | 22.1072 |
| net_avg_loss | -34.7822 |
| avg_hold_time_bars | 8.1627 |
| exposure | 0.3695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
