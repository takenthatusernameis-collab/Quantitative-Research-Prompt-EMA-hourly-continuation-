# EMA Hourly Continuation — SYN/USDT P8_144

**Symbol:** SYN/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.6405 |
| net_win_rate | 0.4464 |
| gross_profit_factor | 0.8369 |
| gross_win_rate | 0.4486 |
| sharpe_ratio | -3.1725 |
| sortino_ratio | -0.9539 |
| max_drawdown | 0.6903 |
| cagr | -0.3640 |
| net_avg_win | 59.3036 |
| net_avg_loss | -74.6586 |
| avg_hold_time_bars | 36.7790 |
| exposure | 0.7640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
