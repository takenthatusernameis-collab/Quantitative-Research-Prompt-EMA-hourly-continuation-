# EMA Hourly Continuation — XYO/USDT P34_55

**Symbol:** XYO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 971 |
| net_profit_factor | 0.3225 |
| net_win_rate | 0.3574 |
| gross_profit_factor | 0.7611 |
| gross_win_rate | 0.3862 |
| sharpe_ratio | -11.8747 |
| sortino_ratio | -5.3081 |
| max_drawdown | 0.9990 |
| cagr | -0.9344 |
| net_avg_win | 13.7012 |
| net_avg_loss | -23.6281 |
| avg_hold_time_bars | 3.6117 |
| exposure | 0.1587 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
