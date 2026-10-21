# EMA Hourly Continuation — CFX/USDT P55_100

**Symbol:** CFX/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.7183 |
| net_win_rate | 0.4892 |
| gross_profit_factor | 0.9476 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -1.8300 |
| sortino_ratio | -0.4724 |
| max_drawdown | 0.4337 |
| cagr | -0.1943 |
| net_avg_win | 67.1613 |
| net_avg_loss | -89.5577 |
| avg_hold_time_bars | 8.5908 |
| exposure | 0.1269 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
