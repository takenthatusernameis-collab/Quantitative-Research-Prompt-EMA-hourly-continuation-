# EMA Hourly Continuation — ANKR/USDT P21_144

**Symbol:** ANKR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.7569 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9508 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -1.9496 |
| sortino_ratio | -0.5446 |
| max_drawdown | 0.5128 |
| cagr | -0.2228 |
| net_avg_win | 79.3841 |
| net_avg_loss | -96.4874 |
| avg_hold_time_bars | 33.1719 |
| exposure | 0.5790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
