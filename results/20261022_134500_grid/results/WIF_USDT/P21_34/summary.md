# EMA Hourly Continuation — WIF/USDT P21_34

**Symbol:** WIF/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1173 |
| net_profit_factor | 0.5024 |
| net_win_rate | 0.4246 |
| gross_profit_factor | 0.8763 |
| gross_win_rate | 0.4450 |
| sharpe_ratio | -9.4243 |
| sortino_ratio | -4.5624 |
| max_drawdown | 0.9966 |
| cagr | -0.8963 |
| net_avg_win | 20.2092 |
| net_avg_loss | -29.6747 |
| avg_hold_time_bars | 2.2975 |
| exposure | 0.1225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
