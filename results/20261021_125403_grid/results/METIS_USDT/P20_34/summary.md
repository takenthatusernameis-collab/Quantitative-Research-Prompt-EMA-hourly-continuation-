# EMA Hourly Continuation — METIS/USDT P20_34

**Symbol:** METIS/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.5956 |
| net_win_rate | 0.4574 |
| gross_profit_factor | 0.8322 |
| gross_win_rate | 0.4574 |
| sharpe_ratio | -3.1249 |
| sortino_ratio | -0.8778 |
| max_drawdown | 0.6498 |
| cagr | -0.3311 |
| net_avg_win | 52.8949 |
| net_avg_loss | -74.8572 |
| avg_hold_time_bars | 5.0207 |
| exposure | 0.0883 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
