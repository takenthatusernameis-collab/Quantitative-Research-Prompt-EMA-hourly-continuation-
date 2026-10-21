# EMA Hourly Continuation — HBAR/USDT P26_100

**Symbol:** HBAR/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.8285 |
| net_win_rate | 0.5181 |
| gross_profit_factor | 1.0720 |
| gross_win_rate | 0.5181 |
| sharpe_ratio | -1.2577 |
| sortino_ratio | -0.3806 |
| max_drawdown | 0.3955 |
| cagr | -0.1615 |
| net_avg_win | 75.4142 |
| net_avg_loss | -97.8600 |
| avg_hold_time_bars | 14.2217 |
| exposure | 0.2857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
