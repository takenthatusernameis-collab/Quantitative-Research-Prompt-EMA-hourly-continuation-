# EMA Hourly Continuation — XMR/USDT P26_200

**Symbol:** XMR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.7871 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 0.9903 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -1.5382 |
| sortino_ratio | -0.4297 |
| max_drawdown | 0.4648 |
| cagr | -0.1797 |
| net_avg_win | 76.6845 |
| net_avg_loss | -95.4050 |
| avg_hold_time_bars | 28.9110 |
| exposure | 0.5020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
