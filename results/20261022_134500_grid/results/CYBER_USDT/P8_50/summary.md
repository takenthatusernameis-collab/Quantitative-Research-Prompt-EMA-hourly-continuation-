# EMA Hourly Continuation — CYBER/USDT P8_50

**Symbol:** CYBER/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1109 |
| net_profit_factor | 0.6318 |
| net_win_rate | 0.4689 |
| gross_profit_factor | 0.9918 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -5.9448 |
| sortino_ratio | -2.7778 |
| max_drawdown | 0.9670 |
| cagr | -0.7407 |
| net_avg_win | 31.8843 |
| net_avg_loss | -44.5546 |
| avg_hold_time_bars | 9.1317 |
| exposure | 0.4603 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
