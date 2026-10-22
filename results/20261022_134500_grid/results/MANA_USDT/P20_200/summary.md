# EMA Hourly Continuation — MANA/USDT P20_200

**Symbol:** MANA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.6534 |
| net_win_rate | 0.4832 |
| gross_profit_factor | 0.9766 |
| gross_win_rate | 0.4916 |
| sharpe_ratio | -2.6185 |
| sortino_ratio | -0.6900 |
| max_drawdown | 0.5920 |
| cagr | -0.2872 |
| net_avg_win | 62.4090 |
| net_avg_loss | -89.3155 |
| avg_hold_time_bars | 40.3687 |
| exposure | 0.6569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
