# EMA Hourly Continuation — REZ/USDT P26_50

**Symbol:** REZ/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.7540 |
| net_win_rate | 0.4883 |
| gross_profit_factor | 0.9787 |
| gross_win_rate | 0.4883 |
| sharpe_ratio | -2.1984 |
| sortino_ratio | -0.6870 |
| max_drawdown | 0.6150 |
| cagr | -0.2703 |
| net_avg_win | 72.1400 |
| net_avg_loss | -91.3108 |
| avg_hold_time_bars | 6.6178 |
| exposure | 0.1438 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
