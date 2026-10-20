# EMA Hourly Continuation — POKT/USDT P144_200

**Symbol:** POKT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.3686 |
| net_win_rate | 0.3671 |
| gross_profit_factor | 0.6396 |
| gross_win_rate | 0.3819 |
| sharpe_ratio | -6.5224 |
| sortino_ratio | -2.0089 |
| max_drawdown | 0.9130 |
| cagr | -0.6189 |
| net_avg_win | 30.6044 |
| net_avg_loss | -48.1590 |
| avg_hold_time_bars | 5.4620 |
| exposure | 0.1172 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
