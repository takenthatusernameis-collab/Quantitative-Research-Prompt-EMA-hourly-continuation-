# EMA Hourly Continuation — NMR/USDT P20_200

**Symbol:** NMR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.7433 |
| net_win_rate | 0.4812 |
| gross_profit_factor | 0.8931 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -1.5524 |
| sortino_ratio | -0.4101 |
| max_drawdown | 0.4226 |
| cagr | -0.1730 |
| net_avg_win | 66.1525 |
| net_avg_loss | -82.5399 |
| avg_hold_time_bars | 39.4464 |
| exposure | 0.6186 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
