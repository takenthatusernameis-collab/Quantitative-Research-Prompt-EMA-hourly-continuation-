# EMA Hourly Continuation — ATH/USDT P144_200

**Symbol:** ATH/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.4725 |
| net_win_rate | 0.4469 |
| gross_profit_factor | 0.8526 |
| gross_win_rate | 0.4565 |
| sharpe_ratio | -5.0637 |
| sortino_ratio | -1.4850 |
| max_drawdown | 0.8328 |
| cagr | -0.5304 |
| net_avg_win | 40.2506 |
| net_avg_loss | -68.8220 |
| avg_hold_time_bars | 3.8140 |
| exposure | 0.0765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
