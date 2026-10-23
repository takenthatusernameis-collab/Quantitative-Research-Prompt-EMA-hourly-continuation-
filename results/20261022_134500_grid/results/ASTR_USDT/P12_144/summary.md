# EMA Hourly Continuation — ASTR/USDT P12_144

**Symbol:** ASTR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.7192 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 1.0375 |
| gross_win_rate | 0.5080 |
| sharpe_ratio | -2.1771 |
| sortino_ratio | -0.6400 |
| max_drawdown | 0.5935 |
| cagr | -0.2606 |
| net_avg_win | 63.8128 |
| net_avg_loss | -85.9156 |
| avg_hold_time_bars | 35.6575 |
| exposure | 0.7019 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
