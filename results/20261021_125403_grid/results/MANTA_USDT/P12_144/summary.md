# EMA Hourly Continuation — MANTA/USDT P12_144

**Symbol:** MANTA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.8204 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 0.9727 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -1.1555 |
| sortino_ratio | -0.3031 |
| max_drawdown | 0.3097 |
| cagr | -0.1315 |
| net_avg_win | 82.0433 |
| net_avg_loss | -97.0833 |
| avg_hold_time_bars | 47.1128 |
| exposure | 0.7217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
