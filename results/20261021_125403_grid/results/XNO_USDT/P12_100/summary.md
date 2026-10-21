# EMA Hourly Continuation — XNO/USDT P12_100

**Symbol:** XNO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.6984 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 0.8566 |
| gross_win_rate | 0.4509 |
| sharpe_ratio | -3.0768 |
| sortino_ratio | -1.0516 |
| max_drawdown | 0.7128 |
| cagr | -0.3839 |
| net_avg_win | 62.2023 |
| net_avg_loss | -73.1465 |
| avg_hold_time_bars | 18.3959 |
| exposure | 0.4858 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
