# EMA Hourly Continuation — LPT/USDT P34_89

**Symbol:** LPT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 742 |
| net_profit_factor | 0.5096 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.7985 |
| gross_win_rate | 0.4515 |
| sharpe_ratio | -5.9088 |
| sortino_ratio | -2.2662 |
| max_drawdown | 0.9361 |
| cagr | -0.6631 |
| net_avg_win | 30.5551 |
| net_avg_loss | -44.9661 |
| avg_hold_time_bars | 7.1469 |
| exposure | 0.2410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
