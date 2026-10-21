# EMA Hourly Continuation — BDX/USDT P12_50

**Symbol:** BDX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.4419 |
| net_win_rate | 0.3973 |
| gross_profit_factor | 0.7025 |
| gross_win_rate | 0.3995 |
| sharpe_ratio | -5.7398 |
| sortino_ratio | -1.7282 |
| max_drawdown | 0.8759 |
| cagr | -0.5569 |
| net_avg_win | 39.1667 |
| net_avg_loss | -58.4222 |
| avg_hold_time_bars | 9.2799 |
| exposure | 0.1869 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
