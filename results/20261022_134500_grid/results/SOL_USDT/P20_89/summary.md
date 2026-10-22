# EMA Hourly Continuation — SOL/USDT P20_89

**Symbol:** SOL/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 697 |
| net_profit_factor | 0.5806 |
| net_win_rate | 0.4634 |
| gross_profit_factor | 0.9823 |
| gross_win_rate | 0.4864 |
| sharpe_ratio | -5.2358 |
| sortino_ratio | -1.9422 |
| max_drawdown | 0.9113 |
| cagr | -0.6101 |
| net_avg_win | 38.8399 |
| net_avg_loss | -57.7709 |
| avg_hold_time_bars | 11.1765 |
| exposure | 0.3541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
