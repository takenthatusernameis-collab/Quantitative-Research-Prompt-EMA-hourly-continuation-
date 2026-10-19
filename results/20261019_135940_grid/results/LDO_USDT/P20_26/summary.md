# EMA Hourly Continuation — LDO/USDT P20_26

**Symbol:** LDO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1253 |
| net_profit_factor | 0.2224 |
| net_win_rate | 0.3591 |
| gross_profit_factor | 0.5699 |
| gross_win_rate | 0.4006 |
| sharpe_ratio | -14.3090 |
| sortino_ratio | -7.3164 |
| max_drawdown | 0.9999 |
| cagr | -0.9792 |
| net_avg_win | 6.3556 |
| net_avg_loss | -16.0142 |
| avg_hold_time_bars | 1.8356 |
| exposure | 0.1045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
