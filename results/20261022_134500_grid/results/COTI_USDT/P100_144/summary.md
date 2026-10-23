# EMA Hourly Continuation — COTI/USDT P100_144

**Symbol:** COTI/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.4966 |
| net_win_rate | 0.4738 |
| gross_profit_factor | 0.8904 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -4.4377 |
| sortino_ratio | -1.3963 |
| max_drawdown | 0.8233 |
| cagr | -0.4926 |
| net_avg_win | 34.3388 |
| net_avg_loss | -62.2586 |
| avg_hold_time_bars | 3.7016 |
| exposure | 0.0835 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
