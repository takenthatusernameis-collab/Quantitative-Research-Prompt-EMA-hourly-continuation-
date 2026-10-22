# EMA Hourly Continuation — KAS/USDT P55_89

**Symbol:** KAS/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.3748 |
| net_win_rate | 0.4327 |
| gross_profit_factor | 0.8149 |
| gross_win_rate | 0.4576 |
| sharpe_ratio | -7.1280 |
| sortino_ratio | -2.6429 |
| max_drawdown | 0.9632 |
| cagr | -0.7296 |
| net_avg_win | 19.4966 |
| net_avg_loss | -39.6817 |
| avg_hold_time_bars | 3.7895 |
| exposure | 0.1178 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
