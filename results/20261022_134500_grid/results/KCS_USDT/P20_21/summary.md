# EMA Hourly Continuation — KCS/USDT P20_21

**Symbol:** KCS/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1184 |
| net_profit_factor | 0.0220 |
| net_win_rate | 0.1394 |
| gross_profit_factor | 0.3233 |
| gross_win_rate | 0.2753 |
| sharpe_ratio | -24.3533 |
| sortino_ratio | -15.5970 |
| max_drawdown | 1.0000 |
| cagr | -0.9998 |
| net_avg_win | 1.3622 |
| net_avg_loss | -10.0341 |
| avg_hold_time_bars | 1.9257 |
| exposure | 0.1036 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
