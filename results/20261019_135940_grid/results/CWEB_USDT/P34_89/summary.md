# EMA Hourly Continuation — CWEB/USDT P34_89

**Symbol:** CWEB/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.4639 |
| net_win_rate | 0.3848 |
| gross_profit_factor | 0.7883 |
| gross_win_rate | 0.3902 |
| sharpe_ratio | -7.3171 |
| sortino_ratio | -2.4187 |
| max_drawdown | 0.9584 |
| cagr | -0.7094 |
| net_avg_win | 38.9800 |
| net_avg_loss | -52.5507 |
| avg_hold_time_bars | 12.2595 |
| exposure | 0.3070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
