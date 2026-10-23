# EMA Hourly Continuation — DEXE/USDT P26_200

**Symbol:** DEXE/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.8041 |
| net_win_rate | 0.5151 |
| gross_profit_factor | 1.0537 |
| gross_win_rate | 0.5217 |
| sharpe_ratio | -1.0176 |
| sortino_ratio | -0.2504 |
| max_drawdown | 0.3427 |
| cagr | -0.1123 |
| net_avg_win | 68.8888 |
| net_avg_loss | -90.9935 |
| avg_hold_time_bars | 50.4348 |
| exposure | 0.6855 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
