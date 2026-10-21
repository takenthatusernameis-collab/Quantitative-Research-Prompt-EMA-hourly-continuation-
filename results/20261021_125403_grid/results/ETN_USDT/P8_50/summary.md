# EMA Hourly Continuation — ETN/USDT P8_50

**Symbol:** ETN/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.5994 |
| net_win_rate | 0.4262 |
| gross_profit_factor | 0.7392 |
| gross_win_rate | 0.4262 |
| sharpe_ratio | -4.1795 |
| sortino_ratio | -1.5027 |
| max_drawdown | 0.7775 |
| cagr | -0.5007 |
| net_avg_win | 49.7167 |
| net_avg_loss | -61.6108 |
| avg_hold_time_bars | 12.7749 |
| exposure | 0.3761 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
