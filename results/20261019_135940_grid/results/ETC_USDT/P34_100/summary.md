# EMA Hourly Continuation — ETC/USDT P34_100

**Symbol:** ETC/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 614 |
| net_profit_factor | 0.5155 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9961 |
| gross_win_rate | 0.5016 |
| sharpe_ratio | -5.0708 |
| sortino_ratio | -1.7589 |
| max_drawdown | 0.8910 |
| cagr | -0.5799 |
| net_avg_win | 31.8680 |
| net_avg_loss | -57.5483 |
| avg_hold_time_bars | 9.7818 |
| exposure | 0.2730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
