# EMA Hourly Continuation — ETN/USDT P26_144

**Symbol:** ETN/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.5671 |
| net_win_rate | 0.4153 |
| gross_profit_factor | 0.6916 |
| gross_win_rate | 0.4153 |
| sharpe_ratio | -3.5098 |
| sortino_ratio | -1.0175 |
| max_drawdown | 0.6382 |
| cagr | -0.3748 |
| net_avg_win | 55.9076 |
| net_avg_loss | -70.0108 |
| avg_hold_time_bars | 20.1610 |
| exposure | 0.3877 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
