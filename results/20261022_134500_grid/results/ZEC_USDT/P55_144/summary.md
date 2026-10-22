# EMA Hourly Continuation — ZEC/USDT P55_144

**Symbol:** ZEC/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.5489 |
| net_win_rate | 0.4612 |
| gross_profit_factor | 0.8594 |
| gross_win_rate | 0.4633 |
| sharpe_ratio | -3.8141 |
| sortino_ratio | -1.1743 |
| max_drawdown | 0.7744 |
| cagr | -0.4402 |
| net_avg_win | 41.2969 |
| net_avg_loss | -64.4062 |
| avg_hold_time_bars | 10.6918 |
| exposure | 0.2381 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
