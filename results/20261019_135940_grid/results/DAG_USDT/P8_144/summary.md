# EMA Hourly Continuation — DAG/USDT P8_144

**Symbol:** DAG/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.5929 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8431 |
| gross_win_rate | 0.4592 |
| sharpe_ratio | -4.1490 |
| sortino_ratio | -1.4622 |
| max_drawdown | 0.8381 |
| cagr | -0.5099 |
| net_avg_win | 41.8470 |
| net_avg_loss | -58.8158 |
| avg_hold_time_bars | 23.4091 |
| exposure | 0.6789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
