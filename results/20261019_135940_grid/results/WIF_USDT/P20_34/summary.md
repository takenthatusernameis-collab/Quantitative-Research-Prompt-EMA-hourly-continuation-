# EMA Hourly Continuation — WIF/USDT P20_34

**Symbol:** WIF/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1189 |
| net_profit_factor | 0.5043 |
| net_win_rate | 0.4239 |
| gross_profit_factor | 0.8635 |
| gross_win_rate | 0.4449 |
| sharpe_ratio | -9.2958 |
| sortino_ratio | -4.5308 |
| max_drawdown | 0.9964 |
| cagr | -0.8935 |
| net_avg_win | 20.1167 |
| net_avg_loss | -29.3471 |
| avg_hold_time_bars | 2.4474 |
| exposure | 0.1323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
