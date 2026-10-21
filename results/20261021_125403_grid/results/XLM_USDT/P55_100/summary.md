# EMA Hourly Continuation — XLM/USDT P55_100

**Symbol:** XLM/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.8727 |
| net_win_rate | 0.5600 |
| gross_profit_factor | 1.2663 |
| gross_win_rate | 0.5600 |
| sharpe_ratio | -0.7259 |
| sortino_ratio | -0.1905 |
| max_drawdown | 0.2548 |
| cagr | -0.0852 |
| net_avg_win | 75.4966 |
| net_avg_loss | -110.0983 |
| avg_hold_time_bars | 8.7323 |
| exposure | 0.1290 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
