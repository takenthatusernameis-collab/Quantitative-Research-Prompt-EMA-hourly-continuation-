# EMA Hourly Continuation — DAG/USDT P20_89

**Symbol:** DAG/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.7774 |
| net_win_rate | 0.4863 |
| gross_profit_factor | 0.9279 |
| gross_win_rate | 0.4863 |
| sharpe_ratio | -1.5440 |
| sortino_ratio | -0.4611 |
| max_drawdown | 0.4721 |
| cagr | -0.1919 |
| net_avg_win | 67.9533 |
| net_avg_loss | -82.7495 |
| avg_hold_time_bars | 15.2420 |
| exposure | 0.3035 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
