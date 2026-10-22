# EMA Hourly Continuation — DAG/USDT P50_89

**Symbol:** DAG/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 259 |
| net_profit_factor | 0.7584 |
| net_win_rate | 0.4865 |
| gross_profit_factor | 0.9390 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -1.3817 |
| sortino_ratio | -0.3174 |
| max_drawdown | 0.3320 |
| cagr | -0.1365 |
| net_avg_win | 76.8108 |
| net_avg_loss | -95.9481 |
| avg_hold_time_bars | 7.4247 |
| exposure | 0.0874 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
