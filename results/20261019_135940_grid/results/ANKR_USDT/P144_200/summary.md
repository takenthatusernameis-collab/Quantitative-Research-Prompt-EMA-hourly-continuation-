# EMA Hourly Continuation — ANKR/USDT P144_200

**Symbol:** ANKR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.3883 |
| net_win_rate | 0.4122 |
| gross_profit_factor | 0.7942 |
| gross_win_rate | 0.4377 |
| sharpe_ratio | -5.9296 |
| sortino_ratio | -1.6729 |
| max_drawdown | 0.8796 |
| cagr | -0.5680 |
| net_avg_win | 34.4239 |
| net_avg_loss | -62.1711 |
| avg_hold_time_bars | 7.3664 |
| exposure | 0.1316 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
