# EMA Hourly Continuation — ENJ/USDT P26_34

**Symbol:** ENJ/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 193 |
| net_profit_factor | 0.7663 |
| net_win_rate | 0.5337 |
| gross_profit_factor | 1.1434 |
| gross_win_rate | 0.5337 |
| sharpe_ratio | -1.1529 |
| sortino_ratio | -0.2311 |
| max_drawdown | 0.2711 |
| cagr | -0.1001 |
| net_avg_win | 74.4044 |
| net_avg_loss | -111.1198 |
| avg_hold_time_bars | 4.3109 |
| exposure | 0.0376 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
