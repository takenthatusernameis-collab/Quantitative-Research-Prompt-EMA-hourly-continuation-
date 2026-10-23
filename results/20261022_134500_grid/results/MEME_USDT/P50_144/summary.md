# EMA Hourly Continuation — MEME/USDT P50_144

**Symbol:** MEME/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.6020 |
| net_win_rate | 0.4633 |
| gross_profit_factor | 0.8567 |
| gross_win_rate | 0.4675 |
| sharpe_ratio | -3.4332 |
| sortino_ratio | -1.0565 |
| max_drawdown | 0.7250 |
| cagr | -0.3947 |
| net_avg_win | 49.0365 |
| net_avg_loss | -70.3215 |
| avg_hold_time_bars | 14.5870 |
| exposure | 0.3163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
