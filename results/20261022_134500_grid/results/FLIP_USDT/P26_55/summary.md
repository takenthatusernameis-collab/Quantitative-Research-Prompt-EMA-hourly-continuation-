# EMA Hourly Continuation — FLIP/USDT P26_55

**Symbol:** FLIP/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 598 |
| net_profit_factor | 0.3579 |
| net_win_rate | 0.3763 |
| gross_profit_factor | 0.7377 |
| gross_win_rate | 0.4197 |
| sharpe_ratio | -8.2571 |
| sortino_ratio | -2.8586 |
| max_drawdown | 0.9763 |
| cagr | -0.7711 |
| net_avg_win | 24.1672 |
| net_avg_loss | -40.7269 |
| avg_hold_time_bars | 8.2793 |
| exposure | 0.2250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
