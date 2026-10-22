# EMA Hourly Continuation — YGG/USDT P50_89

**Symbol:** YGG/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.8117 |
| net_win_rate | 0.5225 |
| gross_profit_factor | 1.0809 |
| gross_win_rate | 0.5225 |
| sharpe_ratio | -1.2555 |
| sortino_ratio | -0.3611 |
| max_drawdown | 0.3653 |
| cagr | -0.1536 |
| net_avg_win | 70.8014 |
| net_avg_loss | -95.4522 |
| avg_hold_time_bars | 7.3900 |
| exposure | 0.1338 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
