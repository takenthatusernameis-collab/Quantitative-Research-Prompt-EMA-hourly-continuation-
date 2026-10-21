# EMA Hourly Continuation — ADA/USDT P34_89

**Symbol:** ADA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.7604 |
| net_win_rate | 0.5048 |
| gross_profit_factor | 1.0094 |
| gross_win_rate | 0.5048 |
| sharpe_ratio | -1.7310 |
| sortino_ratio | -0.5088 |
| max_drawdown | 0.4561 |
| cagr | -0.2082 |
| net_avg_win | 66.3906 |
| net_avg_loss | -88.9948 |
| avg_hold_time_bars | 10.1881 |
| exposure | 0.1945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
