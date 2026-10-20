# EMA Hourly Continuation — SNX/USDT P8_55

**Symbol:** SNX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1042 |
| net_profit_factor | 0.6080 |
| net_win_rate | 0.4722 |
| gross_profit_factor | 0.9575 |
| gross_win_rate | 0.4827 |
| sharpe_ratio | -5.3925 |
| sortino_ratio | -2.4447 |
| max_drawdown | 0.9504 |
| cagr | -0.6906 |
| net_avg_win | 29.8937 |
| net_avg_loss | -43.9802 |
| avg_hold_time_bars | 10.3196 |
| exposure | 0.4866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
