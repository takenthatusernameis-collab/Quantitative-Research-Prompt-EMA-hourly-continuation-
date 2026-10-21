# EMA Hourly Continuation — LDO/USDT P8_89

**Symbol:** LDO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.8113 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9573 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -1.3859 |
| sortino_ratio | -0.4125 |
| max_drawdown | 0.3913 |
| cagr | -0.1749 |
| net_avg_win | 77.2980 |
| net_avg_loss | -91.4174 |
| avg_hold_time_bars | 34.0483 |
| exposure | 0.6732 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
