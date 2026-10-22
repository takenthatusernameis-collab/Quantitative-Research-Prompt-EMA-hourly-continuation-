# EMA Hourly Continuation — LDO/USDT P55_144

**Symbol:** LDO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.6066 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.8431 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -3.5672 |
| sortino_ratio | -1.1077 |
| max_drawdown | 0.7436 |
| cagr | -0.4041 |
| net_avg_win | 50.7491 |
| net_avg_loss | -71.1168 |
| avg_hold_time_bars | 12.5322 |
| exposure | 0.2740 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
