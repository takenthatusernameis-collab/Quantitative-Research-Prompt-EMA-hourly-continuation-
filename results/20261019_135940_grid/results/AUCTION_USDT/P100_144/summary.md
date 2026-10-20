# EMA Hourly Continuation — AUCTION/USDT P100_144

**Symbol:** AUCTION/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.3474 |
| net_win_rate | 0.4082 |
| gross_profit_factor | 0.6991 |
| gross_win_rate | 0.4258 |
| sharpe_ratio | -7.1394 |
| sortino_ratio | -2.2758 |
| max_drawdown | 0.9466 |
| cagr | -0.6865 |
| net_avg_win | 24.0997 |
| net_avg_loss | -47.8567 |
| avg_hold_time_bars | 5.4434 |
| exposure | 0.1261 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
