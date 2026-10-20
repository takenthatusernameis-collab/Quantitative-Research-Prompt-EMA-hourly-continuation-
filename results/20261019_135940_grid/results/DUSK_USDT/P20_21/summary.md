# EMA Hourly Continuation — DUSK/USDT P20_21

**Symbol:** DUSK/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1139 |
| net_profit_factor | 0.1920 |
| net_win_rate | 0.3486 |
| gross_profit_factor | 0.8335 |
| gross_win_rate | 0.4249 |
| sharpe_ratio | -14.6725 |
| sortino_ratio | -7.2275 |
| max_drawdown | 1.0000 |
| cagr | -0.9819 |
| net_avg_win | 5.9842 |
| net_avg_loss | -16.6783 |
| avg_hold_time_bars | 1.7919 |
| exposure | 0.0928 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
