# EMA Hourly Continuation — TURBO/USDT P12_34

**Symbol:** TURBO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1121 |
| net_profit_factor | 0.5727 |
| net_win_rate | 0.4603 |
| gross_profit_factor | 0.9101 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -7.7203 |
| sortino_ratio | -3.9721 |
| max_drawdown | 0.9834 |
| cagr | -0.8575 |
| net_avg_win | 25.5326 |
| net_avg_loss | -38.0252 |
| avg_hold_time_bars | 3.7832 |
| exposure | 0.2314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
