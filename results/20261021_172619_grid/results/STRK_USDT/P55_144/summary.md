# EMA Hourly Continuation — STRK/USDT P55_144

**Symbol:** STRK/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.8862 |
| net_win_rate | 0.5227 |
| gross_profit_factor | 1.0810 |
| gross_win_rate | 0.5227 |
| sharpe_ratio | -0.6368 |
| sortino_ratio | -0.1721 |
| max_drawdown | 0.3093 |
| cagr | -0.0791 |
| net_avg_win | 79.0644 |
| net_avg_loss | -97.7161 |
| avg_hold_time_bars | 13.3494 |
| exposure | 0.2136 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
