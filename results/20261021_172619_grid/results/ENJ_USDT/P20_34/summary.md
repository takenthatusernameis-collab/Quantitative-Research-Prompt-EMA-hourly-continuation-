# EMA Hourly Continuation — ENJ/USDT P20_34

**Symbol:** ENJ/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7113 |
| net_win_rate | 0.5057 |
| gross_profit_factor | 1.0376 |
| gross_win_rate | 0.5057 |
| sharpe_ratio | -2.0864 |
| sortino_ratio | -0.5608 |
| max_drawdown | 0.5118 |
| cagr | -0.2254 |
| net_avg_win | 66.1051 |
| net_avg_loss | -95.0834 |
| avg_hold_time_bars | 4.5600 |
| exposure | 0.0722 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
