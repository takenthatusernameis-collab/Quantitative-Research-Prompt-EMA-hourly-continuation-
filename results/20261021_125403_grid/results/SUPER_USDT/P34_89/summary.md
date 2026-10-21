# EMA Hourly Continuation — SUPER/USDT P34_89

**Symbol:** SUPER/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.8852 |
| net_win_rate | 0.5386 |
| gross_profit_factor | 1.1420 |
| gross_win_rate | 0.5386 |
| sharpe_ratio | -0.6637 |
| sortino_ratio | -0.1983 |
| max_drawdown | 0.2860 |
| cagr | -0.0905 |
| net_avg_win | 71.0250 |
| net_avg_loss | -93.6809 |
| avg_hold_time_bars | 13.2482 |
| exposure | 0.2571 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
