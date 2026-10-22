# EMA Hourly Continuation — BDX/USDT P26_200

**Symbol:** BDX/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 940 |
| net_profit_factor | 0.3715 |
| net_win_rate | 0.3426 |
| gross_profit_factor | 0.7497 |
| gross_win_rate | 0.3883 |
| sharpe_ratio | -12.5136 |
| sortino_ratio | -5.5303 |
| max_drawdown | 0.9995 |
| cagr | -0.9488 |
| net_avg_win | 18.3474 |
| net_avg_loss | -25.7316 |
| avg_hold_time_bars | 9.5660 |
| exposure | 0.4087 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
