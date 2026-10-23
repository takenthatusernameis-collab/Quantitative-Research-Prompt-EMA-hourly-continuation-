# EMA Hourly Continuation — SATS/USDT P12_21

**Symbol:** SATS/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1186 |
| net_profit_factor | 0.4173 |
| net_win_rate | 0.4427 |
| gross_profit_factor | 0.8562 |
| gross_win_rate | 0.4553 |
| sharpe_ratio | -8.7068 |
| sortino_ratio | -4.1915 |
| max_drawdown | 0.9952 |
| cagr | -0.8779 |
| net_avg_win | 13.5721 |
| net_avg_loss | -25.8330 |
| avg_hold_time_bars | 2.7378 |
| exposure | 0.1469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
