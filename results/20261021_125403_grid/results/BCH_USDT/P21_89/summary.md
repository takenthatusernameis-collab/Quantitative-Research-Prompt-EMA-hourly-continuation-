# EMA Hourly Continuation — BCH/USDT P21_89

**Symbol:** BCH/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.6013 |
| net_win_rate | 0.4437 |
| gross_profit_factor | 0.8062 |
| gross_win_rate | 0.4437 |
| sharpe_ratio | -3.5141 |
| sortino_ratio | -1.0637 |
| max_drawdown | 0.7095 |
| cagr | -0.3865 |
| net_avg_win | 53.0325 |
| net_avg_loss | -70.3490 |
| avg_hold_time_bars | 16.6402 |
| exposure | 0.3426 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
