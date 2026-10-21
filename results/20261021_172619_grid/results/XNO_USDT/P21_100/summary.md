# EMA Hourly Continuation — XNO/USDT P21_100

**Symbol:** XNO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.6603 |
| net_win_rate | 0.4427 |
| gross_profit_factor | 0.8243 |
| gross_win_rate | 0.4427 |
| sharpe_ratio | -3.2961 |
| sortino_ratio | -1.0695 |
| max_drawdown | 0.7135 |
| cagr | -0.3891 |
| net_avg_win | 59.4755 |
| net_avg_loss | -71.5686 |
| avg_hold_time_bars | 14.8626 |
| exposure | 0.3540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
