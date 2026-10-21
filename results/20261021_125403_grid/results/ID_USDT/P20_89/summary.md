# EMA Hourly Continuation — ID/USDT P20_89

**Symbol:** ID/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.8015 |
| net_win_rate | 0.5029 |
| gross_profit_factor | 1.0228 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -1.6837 |
| sortino_ratio | -0.5516 |
| max_drawdown | 0.5321 |
| cagr | -0.2248 |
| net_avg_win | 72.4636 |
| net_avg_loss | -91.4533 |
| avg_hold_time_bars | 16.3257 |
| exposure | 0.3879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
