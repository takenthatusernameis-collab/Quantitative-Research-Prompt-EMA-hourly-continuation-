# EMA Hourly Continuation — XTZ/USDT P50_89

**Symbol:** XTZ/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 756 |
| net_profit_factor | 0.4433 |
| net_win_rate | 0.4458 |
| gross_profit_factor | 0.9300 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -6.9754 |
| sortino_ratio | -2.7294 |
| max_drawdown | 0.9648 |
| cagr | -0.7339 |
| net_avg_win | 22.7778 |
| net_avg_loss | -41.3276 |
| avg_hold_time_bars | 4.3505 |
| exposure | 0.1495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
