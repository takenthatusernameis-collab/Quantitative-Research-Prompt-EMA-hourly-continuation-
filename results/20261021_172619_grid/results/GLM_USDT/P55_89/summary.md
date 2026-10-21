# EMA Hourly Continuation — GLM/USDT P55_89

**Symbol:** GLM/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.6243 |
| net_win_rate | 0.4898 |
| gross_profit_factor | 0.9364 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -2.7321 |
| sortino_ratio | -0.7768 |
| max_drawdown | 0.5966 |
| cagr | -0.2989 |
| net_avg_win | 50.8066 |
| net_avg_loss | -78.1401 |
| avg_hold_time_bars | 6.5254 |
| exposure | 0.1169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
