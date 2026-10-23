# EMA Hourly Continuation — WEMIX/USDT P55_89

**Symbol:** WEMIX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1082 |
| net_profit_factor | 0.2044 |
| net_win_rate | 0.2652 |
| gross_profit_factor | 0.4223 |
| gross_win_rate | 0.2865 |
| sharpe_ratio | -16.0263 |
| sortino_ratio | -7.7521 |
| max_drawdown | 1.0000 |
| cagr | -0.9826 |
| net_avg_win | 8.9523 |
| net_avg_loss | -15.8100 |
| avg_hold_time_bars | 3.4399 |
| exposure | 0.1692 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
