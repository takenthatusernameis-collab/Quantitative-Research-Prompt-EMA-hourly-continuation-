# EMA Hourly Continuation — SATS/USDT P21_144

**Symbol:** SATS/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.7030 |
| net_win_rate | 0.4453 |
| gross_profit_factor | 0.8503 |
| gross_win_rate | 0.4478 |
| sharpe_ratio | -2.5279 |
| sortino_ratio | -0.7158 |
| max_drawdown | 0.6326 |
| cagr | -0.2815 |
| net_avg_win | 74.7984 |
| net_avg_loss | -85.4049 |
| avg_hold_time_bars | 25.9527 |
| exposure | 0.4721 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
