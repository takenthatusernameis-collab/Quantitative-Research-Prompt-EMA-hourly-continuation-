# EMA Hourly Continuation — XPR/USDT P20_34

**Symbol:** XPR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 195 |
| net_profit_factor | 0.7395 |
| net_win_rate | 0.5128 |
| gross_profit_factor | 1.0412 |
| gross_win_rate | 0.5128 |
| sharpe_ratio | -1.2988 |
| sortino_ratio | -0.2611 |
| max_drawdown | 0.3010 |
| cagr | -0.1129 |
| net_avg_win | 73.7396 |
| net_avg_loss | -104.9653 |
| avg_hold_time_bars | 10.4923 |
| exposure | 0.0930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
