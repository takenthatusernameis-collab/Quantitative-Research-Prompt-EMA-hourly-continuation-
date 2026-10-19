# EMA Hourly Continuation — AAVE/USDT P100_144

**Symbol:** AAVE/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.4537 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.8739 |
| gross_win_rate | 0.4727 |
| sharpe_ratio | -5.0806 |
| sortino_ratio | -1.5939 |
| max_drawdown | 0.8632 |
| cagr | -0.5454 |
| net_avg_win | 31.3952 |
| net_avg_loss | -59.0914 |
| avg_hold_time_bars | 3.8929 |
| exposure | 0.0876 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
