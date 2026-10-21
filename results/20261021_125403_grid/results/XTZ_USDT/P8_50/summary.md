# EMA Hourly Continuation — XTZ/USDT P8_50

**Symbol:** XTZ/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 717 |
| net_profit_factor | 0.7200 |
| net_win_rate | 0.4951 |
| gross_profit_factor | 0.9697 |
| gross_win_rate | 0.4951 |
| sharpe_ratio | -2.6970 |
| sortino_ratio | -1.0346 |
| max_drawdown | 0.7091 |
| cagr | -0.3780 |
| net_avg_win | 50.4540 |
| net_avg_loss | -68.7176 |
| avg_hold_time_bars | 13.2022 |
| exposure | 0.4303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
