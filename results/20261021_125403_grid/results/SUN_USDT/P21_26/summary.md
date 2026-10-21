# EMA Hourly Continuation — SUN/USDT P21_26

**Symbol:** SUN/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.3058 |
| net_win_rate | 0.3864 |
| gross_profit_factor | 0.7294 |
| gross_win_rate | 0.4159 |
| sharpe_ratio | -7.0287 |
| sortino_ratio | -1.8991 |
| max_drawdown | 0.9112 |
| cagr | -0.6171 |
| net_avg_win | 30.6412 |
| net_avg_loss | -63.1072 |
| avg_hold_time_bars | 5.5339 |
| exposure | 0.0849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
