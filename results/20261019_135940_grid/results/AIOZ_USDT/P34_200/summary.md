# EMA Hourly Continuation — AIOZ/USDT P34_200

**Symbol:** AIOZ/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.6899 |
| net_win_rate | 0.4699 |
| gross_profit_factor | 0.9180 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -2.7905 |
| sortino_ratio | -0.8214 |
| max_drawdown | 0.6711 |
| cagr | -0.3192 |
| net_avg_win | 67.8643 |
| net_avg_loss | -87.2025 |
| avg_hold_time_bars | 26.3681 |
| exposure | 0.5178 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
