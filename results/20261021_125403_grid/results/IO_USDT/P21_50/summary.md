# EMA Hourly Continuation — IO/USDT P21_50

**Symbol:** IO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.7929 |
| net_win_rate | 0.4919 |
| gross_profit_factor | 0.9790 |
| gross_win_rate | 0.4919 |
| sharpe_ratio | -1.6654 |
| sortino_ratio | -0.5103 |
| max_drawdown | 0.4477 |
| cagr | -0.2102 |
| net_avg_win | 77.0656 |
| net_avg_loss | -94.0852 |
| avg_hold_time_bars | 7.6473 |
| exposure | 0.1596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
