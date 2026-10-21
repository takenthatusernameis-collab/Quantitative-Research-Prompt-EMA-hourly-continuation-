# EMA Hourly Continuation — DAG/USDT P26_89

**Symbol:** DAG/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.7978 |
| net_win_rate | 0.4861 |
| gross_profit_factor | 0.9539 |
| gross_win_rate | 0.4861 |
| sharpe_ratio | -1.5068 |
| sortino_ratio | -0.4272 |
| max_drawdown | 0.4461 |
| cagr | -0.1797 |
| net_avg_win | 80.5618 |
| net_avg_loss | -95.5030 |
| avg_hold_time_bars | 12.8228 |
| exposure | 0.2302 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
