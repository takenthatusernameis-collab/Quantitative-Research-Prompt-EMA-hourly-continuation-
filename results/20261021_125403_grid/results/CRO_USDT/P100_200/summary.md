# EMA Hourly Continuation — CRO/USDT P100_200

**Symbol:** CRO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 252 |
| net_profit_factor | 0.6301 |
| net_win_rate | 0.4762 |
| gross_profit_factor | 0.8971 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -2.2012 |
| sortino_ratio | -0.4997 |
| max_drawdown | 0.4741 |
| cagr | -0.2053 |
| net_avg_win | 62.2462 |
| net_avg_loss | -89.8038 |
| avg_hold_time_bars | 15.0476 |
| exposure | 0.1724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
