# EMA Hourly Continuation — BTC/USDT P12_144

**Symbol:** BTC/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.7198 |
| net_win_rate | 0.5145 |
| gross_profit_factor | 1.0414 |
| gross_win_rate | 0.5145 |
| sharpe_ratio | -1.8080 |
| sortino_ratio | -0.4730 |
| max_drawdown | 0.4749 |
| cagr | -0.1949 |
| net_avg_win | 60.7699 |
| net_avg_loss | -89.4739 |
| avg_hold_time_bars | 44.2243 |
| exposure | 0.6704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
