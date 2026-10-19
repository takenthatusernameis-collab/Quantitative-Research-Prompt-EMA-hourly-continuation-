# EMA Hourly Continuation — ZK/USDT P55_89

**Symbol:** ZK/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 673 |
| net_profit_factor | 0.5120 |
| net_win_rate | 0.4458 |
| gross_profit_factor | 0.8864 |
| gross_win_rate | 0.4591 |
| sharpe_ratio | -6.0966 |
| sortino_ratio | -2.2986 |
| max_drawdown | 0.9316 |
| cagr | -0.6789 |
| net_avg_win | 32.5280 |
| net_avg_loss | -51.0952 |
| avg_hold_time_bars | 4.4799 |
| exposure | 0.1470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
