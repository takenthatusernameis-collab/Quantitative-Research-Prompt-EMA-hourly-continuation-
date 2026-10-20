# EMA Hourly Continuation — VELO/USDT P12_200

**Symbol:** VELO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.7940 |
| net_win_rate | 0.5057 |
| gross_profit_factor | 1.0018 |
| gross_win_rate | 0.5080 |
| sharpe_ratio | -1.3532 |
| sortino_ratio | -0.4026 |
| max_drawdown | 0.4912 |
| cagr | -0.1733 |
| net_avg_win | 66.2487 |
| net_avg_loss | -85.3727 |
| avg_hold_time_bars | 35.2746 |
| exposure | 0.7007 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
