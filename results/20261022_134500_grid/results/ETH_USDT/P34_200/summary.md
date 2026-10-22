# EMA Hourly Continuation — ETH/USDT P34_200

**Symbol:** ETH/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.4064 |
| net_win_rate | 0.4377 |
| gross_profit_factor | 0.7894 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -4.2469 |
| sortino_ratio | -1.0245 |
| max_drawdown | 0.7334 |
| cagr | -0.4027 |
| net_avg_win | 38.2235 |
| net_avg_loss | -73.2232 |
| avg_hold_time_bars | 44.5118 |
| exposure | 0.6009 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
