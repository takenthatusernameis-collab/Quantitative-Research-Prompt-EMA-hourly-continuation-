# EMA Hourly Continuation — BONK/USDT P144_200

**Symbol:** BONK/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 157 |
| net_profit_factor | 0.6616 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.8299 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -1.5503 |
| sortino_ratio | -0.2762 |
| max_drawdown | 0.2795 |
| cagr | -0.1191 |
| net_avg_win | 74.0557 |
| net_avg_loss | -94.8126 |
| avg_hold_time_bars | 8.8917 |
| exposure | 0.0635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
