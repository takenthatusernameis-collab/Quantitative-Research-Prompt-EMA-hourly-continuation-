# EMA Hourly Continuation — LINK/USDT P12_200

**Symbol:** LINK/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.6756 |
| net_win_rate | 0.5076 |
| gross_profit_factor | 1.0592 |
| gross_win_rate | 0.5178 |
| sharpe_ratio | -2.2934 |
| sortino_ratio | -0.6305 |
| max_drawdown | 0.5568 |
| cagr | -0.2681 |
| net_avg_win | 56.5825 |
| net_avg_loss | -86.3418 |
| avg_hold_time_bars | 39.3426 |
| exposure | 0.7046 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
