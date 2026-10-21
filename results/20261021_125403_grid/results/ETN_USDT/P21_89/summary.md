# EMA Hourly Continuation — ETN/USDT P21_89

**Symbol:** ETN/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.5623 |
| net_win_rate | 0.4095 |
| gross_profit_factor | 0.6976 |
| gross_win_rate | 0.4095 |
| sharpe_ratio | -4.0035 |
| sortino_ratio | -1.2312 |
| max_drawdown | 0.7038 |
| cagr | -0.4346 |
| net_avg_win | 55.0405 |
| net_avg_loss | -67.8920 |
| avg_hold_time_bars | 14.4221 |
| exposure | 0.3118 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
