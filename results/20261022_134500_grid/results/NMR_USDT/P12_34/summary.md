# EMA Hourly Continuation — NMR/USDT P12_34

**Symbol:** NMR/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1345 |
| net_profit_factor | 0.4978 |
| net_win_rate | 0.4357 |
| gross_profit_factor | 0.9409 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -9.7027 |
| sortino_ratio | -5.0073 |
| max_drawdown | 0.9982 |
| cagr | -0.9174 |
| net_avg_win | 16.8807 |
| net_avg_loss | -26.1832 |
| avg_hold_time_bars | 4.0900 |
| exposure | 0.2500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
