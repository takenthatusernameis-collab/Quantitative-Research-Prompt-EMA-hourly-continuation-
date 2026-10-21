# EMA Hourly Continuation — GLM/USDT P8_21

**Symbol:** GLM/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 791 |
| net_profit_factor | 0.6605 |
| net_win_rate | 0.5006 |
| gross_profit_factor | 1.0106 |
| gross_win_rate | 0.5019 |
| sharpe_ratio | -3.9683 |
| sortino_ratio | -1.6058 |
| max_drawdown | 0.8448 |
| cagr | -0.5195 |
| net_avg_win | 41.3364 |
| net_avg_loss | -62.7389 |
| avg_hold_time_bars | 5.5057 |
| exposure | 0.1980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
