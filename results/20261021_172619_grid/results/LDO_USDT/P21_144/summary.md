# EMA Hourly Continuation — LDO/USDT P21_144

**Symbol:** LDO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.7753 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9107 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -1.5074 |
| sortino_ratio | -0.4072 |
| max_drawdown | 0.4049 |
| cagr | -0.1721 |
| net_avg_win | 75.3116 |
| net_avg_loss | -89.3887 |
| avg_hold_time_bars | 32.8283 |
| exposure | 0.5387 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
