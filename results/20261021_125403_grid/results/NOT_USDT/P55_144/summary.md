# EMA Hourly Continuation — NOT/USDT P55_144

**Symbol:** NOT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.7599 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9302 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -1.6597 |
| sortino_ratio | -0.4324 |
| max_drawdown | 0.4040 |
| cagr | -0.1810 |
| net_avg_win | 78.5052 |
| net_avg_loss | -95.3106 |
| avg_hold_time_bars | 15.0495 |
| exposure | 0.2283 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
