# EMA Hourly Continuation — TRADE/USDT P100_144

**Symbol:** TRADE/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.3509 |
| net_win_rate | 0.3603 |
| gross_profit_factor | 0.5593 |
| gross_win_rate | 0.3629 |
| sharpe_ratio | -6.0923 |
| sortino_ratio | -1.6924 |
| max_drawdown | 0.8767 |
| cagr | -0.5615 |
| net_avg_win | 34.2307 |
| net_avg_loss | -54.9475 |
| avg_hold_time_bars | 5.2454 |
| exposure | 0.0913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
