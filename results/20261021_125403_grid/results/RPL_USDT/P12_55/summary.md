# EMA Hourly Continuation — RPL/USDT P12_55

**Symbol:** RPL/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.7646 |
| net_win_rate | 0.4881 |
| gross_profit_factor | 0.9768 |
| gross_win_rate | 0.4881 |
| sharpe_ratio | -2.4230 |
| sortino_ratio | -0.8963 |
| max_drawdown | 0.6579 |
| cagr | -0.3380 |
| net_avg_win | 63.8539 |
| net_avg_loss | -79.6379 |
| avg_hold_time_bars | 13.3234 |
| exposure | 0.4064 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
