# EMA Hourly Continuation — ERG/USDT P26_50

**Symbol:** ERG/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 938 |
| net_profit_factor | 0.2459 |
| net_win_rate | 0.3465 |
| gross_profit_factor | 0.4929 |
| gross_win_rate | 0.3689 |
| sharpe_ratio | -11.5152 |
| sortino_ratio | -5.0582 |
| max_drawdown | 0.9984 |
| cagr | -0.9225 |
| net_avg_win | 10.0181 |
| net_avg_loss | -21.5980 |
| avg_hold_time_bars | 3.9414 |
| exposure | 0.1680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
