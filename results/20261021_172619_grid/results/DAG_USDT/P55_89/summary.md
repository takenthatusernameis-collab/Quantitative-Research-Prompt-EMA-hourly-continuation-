# EMA Hourly Continuation — DAG/USDT P55_89

**Symbol:** DAG/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 211 |
| net_profit_factor | 0.7030 |
| net_win_rate | 0.4692 |
| gross_profit_factor | 0.8748 |
| gross_win_rate | 0.4692 |
| sharpe_ratio | -1.5774 |
| sortino_ratio | -0.3260 |
| max_drawdown | 0.3322 |
| cagr | -0.1399 |
| net_avg_win | 75.3403 |
| net_avg_loss | -94.7266 |
| avg_hold_time_bars | 6.9905 |
| exposure | 0.0670 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
