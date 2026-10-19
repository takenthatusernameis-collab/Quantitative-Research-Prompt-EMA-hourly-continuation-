# EMA Hourly Continuation — TAO/USDT P20_200

**Symbol:** TAO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.7755 |
| net_win_rate | 0.4963 |
| gross_profit_factor | 1.0115 |
| gross_win_rate | 0.5012 |
| sharpe_ratio | -1.7172 |
| sortino_ratio | -0.4875 |
| max_drawdown | 0.5173 |
| cagr | -0.2075 |
| net_avg_win | 75.6564 |
| net_avg_loss | -96.1309 |
| avg_hold_time_bars | 33.1720 |
| exposure | 0.6137 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
