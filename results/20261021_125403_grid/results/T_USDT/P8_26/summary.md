# EMA Hourly Continuation — T/USDT P8_26

**Symbol:** T/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 779 |
| net_profit_factor | 0.6857 |
| net_win_rate | 0.4917 |
| gross_profit_factor | 1.0400 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -3.9606 |
| sortino_ratio | -1.5839 |
| max_drawdown | 0.8476 |
| cagr | -0.5147 |
| net_avg_win | 47.7733 |
| net_avg_loss | -67.3811 |
| avg_hold_time_bars | 7.6123 |
| exposure | 0.2684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
