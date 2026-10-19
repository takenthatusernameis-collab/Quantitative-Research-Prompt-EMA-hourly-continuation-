# EMA Hourly Continuation — BTT/USDT P26_200

**Symbol:** BTT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.4051 |
| net_win_rate | 0.4140 |
| gross_profit_factor | 0.7298 |
| gross_win_rate | 0.4351 |
| sharpe_ratio | -4.4830 |
| sortino_ratio | -1.0519 |
| max_drawdown | 0.7477 |
| cagr | -0.4186 |
| net_avg_win | 42.9258 |
| net_avg_loss | -74.8711 |
| avg_hold_time_bars | 48.1895 |
| exposure | 0.6243 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
