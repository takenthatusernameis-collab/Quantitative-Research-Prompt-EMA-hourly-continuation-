# EMA Hourly Continuation — GLM/USDT P20_89

**Symbol:** GLM/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.6796 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 0.9032 |
| gross_win_rate | 0.4779 |
| sharpe_ratio | -2.7564 |
| sortino_ratio | -0.9151 |
| max_drawdown | 0.6626 |
| cagr | -0.3427 |
| net_avg_win | 53.5480 |
| net_avg_loss | -71.5798 |
| avg_hold_time_bars | 16.4059 |
| exposure | 0.4042 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
