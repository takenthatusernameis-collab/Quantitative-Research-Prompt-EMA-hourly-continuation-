# EMA Hourly Continuation — GLM/USDT P34_89

**Symbol:** GLM/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 690 |
| net_profit_factor | 0.5363 |
| net_win_rate | 0.4739 |
| gross_profit_factor | 0.9158 |
| gross_win_rate | 0.4928 |
| sharpe_ratio | -4.7962 |
| sortino_ratio | -1.7821 |
| max_drawdown | 0.8873 |
| cagr | -0.5751 |
| net_avg_win | 31.2425 |
| net_avg_loss | -52.4814 |
| avg_hold_time_bars | 7.8464 |
| exposure | 0.2461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
