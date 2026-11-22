# EMA Hourly Continuation — AZERO/USDT P12_55

**Symbol:** AZERO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 909 |
| net_profit_factor | 0.6166 |
| net_win_rate | 0.4675 |
| gross_profit_factor | 1.0059 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -5.0244 |
| sortino_ratio | -2.1063 |
| max_drawdown | 0.9315 |
| cagr | -0.6452 |
| net_avg_win | 35.0759 |
| net_avg_loss | -49.9479 |
| avg_hold_time_bars | 9.1287 |
| exposure | 0.3755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
