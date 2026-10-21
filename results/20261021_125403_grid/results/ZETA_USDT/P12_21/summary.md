# EMA Hourly Continuation — ZETA/USDT P12_21

**Symbol:** ZETA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.6746 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9629 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -2.9287 |
| sortino_ratio | -0.8959 |
| max_drawdown | 0.6643 |
| cagr | -0.3357 |
| net_avg_win | 60.3645 |
| net_avg_loss | -83.4468 |
| avg_hold_time_bars | 4.7598 |
| exposure | 0.0986 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
