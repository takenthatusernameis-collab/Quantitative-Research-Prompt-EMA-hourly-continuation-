# EMA Hourly Continuation — STRAX/USDT P8_26

**Symbol:** STRAX/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 812 |
| net_profit_factor | 0.5440 |
| net_win_rate | 0.4433 |
| gross_profit_factor | 0.7843 |
| gross_win_rate | 0.4433 |
| sharpe_ratio | -5.5648 |
| sortino_ratio | -2.2656 |
| max_drawdown | 0.9289 |
| cagr | -0.6496 |
| net_avg_win | 30.7169 |
| net_avg_loss | -44.9757 |
| avg_hold_time_bars | 7.1207 |
| exposure | 0.2644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
