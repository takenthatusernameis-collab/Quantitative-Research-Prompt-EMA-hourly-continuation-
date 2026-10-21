# EMA Hourly Continuation — RENDER/USDT P20_50

**Symbol:** RENDER/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.7718 |
| net_win_rate | 0.5060 |
| gross_profit_factor | 1.0083 |
| gross_win_rate | 0.5060 |
| sharpe_ratio | -1.7256 |
| sortino_ratio | -0.5430 |
| max_drawdown | 0.4609 |
| cagr | -0.2209 |
| net_avg_win | 67.1758 |
| net_avg_loss | -89.1649 |
| avg_hold_time_bars | 6.7759 |
| exposure | 0.1484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
