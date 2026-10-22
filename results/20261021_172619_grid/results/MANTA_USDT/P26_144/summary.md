# EMA Hourly Continuation — MANTA/USDT P26_144

**Symbol:** MANTA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.7691 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 0.9134 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -1.5473 |
| sortino_ratio | -0.4159 |
| max_drawdown | 0.3828 |
| cagr | -0.1748 |
| net_avg_win | 74.9977 |
| net_avg_loss | -89.1246 |
| avg_hold_time_bars | 31.7135 |
| exposure | 0.5132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
