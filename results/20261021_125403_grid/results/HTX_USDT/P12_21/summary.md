# EMA Hourly Continuation — HTX/USDT P12_21

**Symbol:** HTX/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.2914 |
| net_win_rate | 0.3320 |
| gross_profit_factor | 0.5571 |
| gross_win_rate | 0.3402 |
| sharpe_ratio | -8.7236 |
| sortino_ratio | -2.8223 |
| max_drawdown | 0.9669 |
| cagr | -0.7410 |
| net_avg_win | 24.6981 |
| net_avg_loss | -42.1151 |
| avg_hold_time_bars | 5.3526 |
| exposure | 0.1175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
