# EMA Hourly Continuation — VET/USDT P8_21

**Symbol:** VET/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1678 |
| net_profit_factor | 0.3030 |
| net_win_rate | 0.4166 |
| gross_profit_factor | 0.7387 |
| gross_win_rate | 0.4458 |
| sharpe_ratio | -12.8759 |
| sortino_ratio | -7.4486 |
| max_drawdown | 0.9999 |
| cagr | -0.9776 |
| net_avg_win | 6.2194 |
| net_avg_loss | -14.6544 |
| avg_hold_time_bars | 2.8754 |
| exposure | 0.2193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
