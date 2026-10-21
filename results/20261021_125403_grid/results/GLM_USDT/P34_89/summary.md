# EMA Hourly Continuation — GLM/USDT P34_89

**Symbol:** GLM/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.7848 |
| net_win_rate | 0.5298 |
| gross_profit_factor | 1.1103 |
| gross_win_rate | 0.5317 |
| sharpe_ratio | -1.5599 |
| sortino_ratio | -0.5045 |
| max_drawdown | 0.4677 |
| cagr | -0.2073 |
| net_avg_win | 60.3755 |
| net_avg_loss | -86.6701 |
| avg_hold_time_bars | 10.1329 |
| exposure | 0.2321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
