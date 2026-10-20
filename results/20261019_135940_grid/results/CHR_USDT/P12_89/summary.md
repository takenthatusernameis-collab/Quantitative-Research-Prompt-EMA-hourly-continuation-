# EMA Hourly Continuation — CHR/USDT P12_89

**Symbol:** CHR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.6500 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.8980 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -3.6040 |
| sortino_ratio | -1.3147 |
| max_drawdown | 0.8024 |
| cagr | -0.4621 |
| net_avg_win | 46.7659 |
| net_avg_loss | -63.4596 |
| avg_hold_time_bars | 19.0881 |
| exposure | 0.5787 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
