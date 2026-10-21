# EMA Hourly Continuation — FLR/USDT P26_144

**Symbol:** FLR/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.6491 |
| net_win_rate | 0.4570 |
| gross_profit_factor | 0.8321 |
| gross_win_rate | 0.4570 |
| sharpe_ratio | -2.8711 |
| sortino_ratio | -0.8679 |
| max_drawdown | 0.6407 |
| cagr | -0.3292 |
| net_avg_win | 56.5752 |
| net_avg_loss | -73.3428 |
| avg_hold_time_bars | 19.7042 |
| exposure | 0.4057 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
