# EMA Hourly Continuation — AVA/USDT P55_100

**Symbol:** AVA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.7768 |
| net_win_rate | 0.5159 |
| gross_profit_factor | 1.0535 |
| gross_win_rate | 0.5159 |
| sharpe_ratio | -1.4955 |
| sortino_ratio | -0.4187 |
| max_drawdown | 0.4213 |
| cagr | -0.1752 |
| net_avg_win | 68.4564 |
| net_avg_loss | -93.8998 |
| avg_hold_time_bars | 7.2619 |
| exposure | 0.1248 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
