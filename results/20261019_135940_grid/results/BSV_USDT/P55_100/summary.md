# EMA Hourly Continuation — BSV/USDT P55_100

**Symbol:** BSV/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.4139 |
| net_win_rate | 0.4187 |
| gross_profit_factor | 0.8126 |
| gross_win_rate | 0.4378 |
| sharpe_ratio | -7.2839 |
| sortino_ratio | -2.6790 |
| max_drawdown | 0.9657 |
| cagr | -0.7373 |
| net_avg_win | 23.8286 |
| net_avg_loss | -41.4776 |
| avg_hold_time_bars | 5.6384 |
| exposure | 0.1750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
