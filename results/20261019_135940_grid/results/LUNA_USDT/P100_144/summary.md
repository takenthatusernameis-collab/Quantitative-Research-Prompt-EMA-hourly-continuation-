# EMA Hourly Continuation — LUNA/USDT P100_144

**Symbol:** LUNA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 593 |
| net_profit_factor | 0.3492 |
| net_win_rate | 0.4064 |
| gross_profit_factor | 0.7400 |
| gross_win_rate | 0.4266 |
| sharpe_ratio | -7.5513 |
| sortino_ratio | -2.6264 |
| max_drawdown | 0.9630 |
| cagr | -0.7295 |
| net_avg_win | 21.4304 |
| net_avg_loss | -42.0164 |
| avg_hold_time_bars | 4.2479 |
| exposure | 0.1145 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
