# EMA Hourly Continuation — RENDER/USDT P8_50

**Symbol:** RENDER/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1029 |
| net_profit_factor | 0.6012 |
| net_win_rate | 0.4762 |
| gross_profit_factor | 0.9066 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -5.7439 |
| sortino_ratio | -2.7902 |
| max_drawdown | 0.9499 |
| cagr | -0.7394 |
| net_avg_win | 29.0874 |
| net_avg_loss | -43.9839 |
| avg_hold_time_bars | 7.9631 |
| exposure | 0.4325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
