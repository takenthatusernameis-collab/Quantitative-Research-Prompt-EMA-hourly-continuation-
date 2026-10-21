# EMA Hourly Continuation — DGB/USDT P12_21

**Symbol:** DGB/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.7665 |
| net_win_rate | 0.5166 |
| gross_profit_factor | 1.0965 |
| gross_win_rate | 0.5166 |
| sharpe_ratio | -1.5575 |
| sortino_ratio | -0.3897 |
| max_drawdown | 0.4244 |
| cagr | -0.1638 |
| net_avg_win | 76.1434 |
| net_avg_loss | -106.1441 |
| avg_hold_time_bars | 5.5033 |
| exposure | 0.0755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
