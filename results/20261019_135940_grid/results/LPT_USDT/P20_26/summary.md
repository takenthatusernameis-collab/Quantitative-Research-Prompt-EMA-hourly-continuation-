# EMA Hourly Continuation — LPT/USDT P20_26

**Symbol:** LPT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1295 |
| net_profit_factor | 0.3136 |
| net_win_rate | 0.3768 |
| gross_profit_factor | 0.7581 |
| gross_win_rate | 0.4247 |
| sharpe_ratio | -14.1108 |
| sortino_ratio | -7.3440 |
| max_drawdown | 0.9999 |
| cagr | -0.9785 |
| net_avg_win | 9.3604 |
| net_avg_loss | -18.0511 |
| avg_hold_time_bars | 2.0680 |
| exposure | 0.1217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
