# EMA Hourly Continuation — MAGIC/USDT P8_50

**Symbol:** MAGIC/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1015 |
| net_profit_factor | 0.6402 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 1.0157 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -5.4366 |
| sortino_ratio | -2.4413 |
| max_drawdown | 0.9469 |
| cagr | -0.6867 |
| net_avg_win | 35.4330 |
| net_avg_loss | -48.6819 |
| avg_hold_time_bars | 10.2020 |
| exposure | 0.4707 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
