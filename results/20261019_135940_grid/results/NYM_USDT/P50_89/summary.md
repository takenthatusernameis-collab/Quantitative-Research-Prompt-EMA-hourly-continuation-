# EMA Hourly Continuation — NYM/USDT P50_89

**Symbol:** NYM/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 564 |
| net_profit_factor | 0.1944 |
| net_win_rate | 0.3191 |
| gross_profit_factor | 0.5302 |
| gross_win_rate | 0.3564 |
| sharpe_ratio | -10.2552 |
| sortino_ratio | -3.5509 |
| max_drawdown | 0.9915 |
| cagr | -0.8485 |
| net_avg_win | 13.2871 |
| net_avg_loss | -32.0424 |
| avg_hold_time_bars | 6.0035 |
| exposure | 0.1539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
