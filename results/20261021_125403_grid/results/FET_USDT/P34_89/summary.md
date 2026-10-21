# EMA Hourly Continuation — FET/USDT P34_89

**Symbol:** FET/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.7933 |
| net_win_rate | 0.4944 |
| gross_profit_factor | 0.9710 |
| gross_win_rate | 0.4944 |
| sharpe_ratio | -1.3065 |
| sortino_ratio | -0.3526 |
| max_drawdown | 0.3697 |
| cagr | -0.1504 |
| net_avg_win | 73.2236 |
| net_avg_loss | -90.2555 |
| avg_hold_time_bars | 14.1910 |
| exposure | 0.2296 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
