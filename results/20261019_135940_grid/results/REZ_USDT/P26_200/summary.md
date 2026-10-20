# EMA Hourly Continuation — REZ/USDT P26_200

**Symbol:** REZ/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.8646 |
| net_win_rate | 0.5163 |
| gross_profit_factor | 1.1059 |
| gross_win_rate | 0.5263 |
| sharpe_ratio | -0.9299 |
| sortino_ratio | -0.2679 |
| max_drawdown | 0.3559 |
| cagr | -0.1200 |
| net_avg_win | 84.0600 |
| net_avg_loss | -103.7749 |
| avg_hold_time_bars | 31.8546 |
| exposure | 0.5864 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
