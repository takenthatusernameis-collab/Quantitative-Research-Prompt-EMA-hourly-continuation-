# EMA Hourly Continuation — ARB/USDT P8_89

**Symbol:** ARB/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.6120 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.9341 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -3.7038 |
| sortino_ratio | -1.3098 |
| max_drawdown | 0.7996 |
| cagr | -0.4715 |
| net_avg_win | 41.2908 |
| net_avg_loss | -62.1682 |
| avg_hold_time_bars | 23.6006 |
| exposure | 0.6823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
