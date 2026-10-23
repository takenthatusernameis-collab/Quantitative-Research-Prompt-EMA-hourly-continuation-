# EMA Hourly Continuation — ZKJ/USDT P21_55

**Symbol:** ZKJ/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1049 |
| net_profit_factor | 0.1751 |
| net_win_rate | 0.3031 |
| gross_profit_factor | 0.4740 |
| gross_win_rate | 0.3689 |
| sharpe_ratio | -14.6353 |
| sortino_ratio | -6.9084 |
| max_drawdown | 0.9999 |
| cagr | -0.9760 |
| net_avg_win | 6.6732 |
| net_avg_loss | -16.5817 |
| avg_hold_time_bars | 8.2097 |
| exposure | 0.3915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
