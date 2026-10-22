# EMA Hourly Continuation — MANTA/USDT P50_55

**Symbol:** MANTA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 136 |
| net_profit_factor | 0.7263 |
| net_win_rate | 0.5074 |
| gross_profit_factor | 1.0395 |
| gross_win_rate | 0.5074 |
| sharpe_ratio | -1.2191 |
| sortino_ratio | -0.2042 |
| max_drawdown | 0.2828 |
| cagr | -0.0897 |
| net_avg_win | 80.8047 |
| net_avg_loss | -114.5830 |
| avg_hold_time_bars | 5.7500 |
| exposure | 0.0355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
