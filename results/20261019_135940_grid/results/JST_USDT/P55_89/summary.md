# EMA Hourly Continuation — JST/USDT P55_89

**Symbol:** JST/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 579 |
| net_profit_factor | 0.2474 |
| net_win_rate | 0.4231 |
| gross_profit_factor | 0.9030 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -8.1197 |
| sortino_ratio | -2.8109 |
| max_drawdown | 0.9739 |
| cagr | -0.7643 |
| net_avg_win | 13.0664 |
| net_avg_loss | -38.7434 |
| avg_hold_time_bars | 5.0052 |
| exposure | 0.1311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
