# EMA Hourly Continuation — VET/USDT P12_50

**Symbol:** VET/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.7111 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 0.9477 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -2.5961 |
| sortino_ratio | -0.9527 |
| max_drawdown | 0.6827 |
| cagr | -0.3540 |
| net_avg_win | 50.6117 |
| net_avg_loss | -69.2502 |
| avg_hold_time_bars | 9.8554 |
| exposure | 0.2943 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
