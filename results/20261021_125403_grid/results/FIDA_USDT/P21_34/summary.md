# EMA Hourly Continuation — FIDA/USDT P21_34

**Symbol:** FIDA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.6422 |
| net_win_rate | 0.4883 |
| gross_profit_factor | 0.9450 |
| gross_win_rate | 0.4904 |
| sharpe_ratio | -2.9921 |
| sortino_ratio | -0.9281 |
| max_drawdown | 0.6596 |
| cagr | -0.3475 |
| net_avg_win | 51.4607 |
| net_avg_loss | -76.4711 |
| avg_hold_time_bars | 5.5138 |
| exposure | 0.1175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
