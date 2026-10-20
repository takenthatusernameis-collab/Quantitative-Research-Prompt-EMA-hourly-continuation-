# EMA Hourly Continuation — VR/USDT P89_144

**Symbol:** VR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 620 |
| net_profit_factor | 0.3233 |
| net_win_rate | 0.2565 |
| gross_profit_factor | 0.5465 |
| gross_win_rate | 0.2661 |
| sharpe_ratio | -12.3086 |
| sortino_ratio | -4.4684 |
| max_drawdown | 0.9985 |
| cagr | -0.9238 |
| net_avg_win | 29.9947 |
| net_avg_loss | -32.0034 |
| avg_hold_time_bars | 4.9774 |
| exposure | 0.1403 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
