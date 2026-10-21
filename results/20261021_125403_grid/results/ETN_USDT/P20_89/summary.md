# EMA Hourly Continuation — ETN/USDT P20_89

**Symbol:** ETN/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 405 |
| net_profit_factor | 0.5540 |
| net_win_rate | 0.4049 |
| gross_profit_factor | 0.6858 |
| gross_win_rate | 0.4049 |
| sharpe_ratio | -4.1540 |
| sortino_ratio | -1.2879 |
| max_drawdown | 0.7198 |
| cagr | -0.4493 |
| net_avg_win | 54.1330 |
| net_avg_loss | -66.4885 |
| avg_hold_time_bars | 14.3975 |
| exposure | 0.3167 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
