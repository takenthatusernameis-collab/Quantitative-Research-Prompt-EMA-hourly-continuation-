# EMA Hourly Continuation — BONK/USDT P26_144

**Symbol:** BONK/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.8612 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 0.9937 |
| gross_win_rate | 0.5045 |
| sharpe_ratio | -0.7826 |
| sortino_ratio | -0.2056 |
| max_drawdown | 0.3632 |
| cagr | -0.0932 |
| net_avg_win | 79.9408 |
| net_avg_loss | -93.3814 |
| avg_hold_time_bars | 32.1306 |
| exposure | 0.4922 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
