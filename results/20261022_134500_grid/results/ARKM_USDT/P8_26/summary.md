# EMA Hourly Continuation — ARKM/USDT P8_26

**Symbol:** ARKM/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1611 |
| net_profit_factor | 0.5080 |
| net_win_rate | 0.4196 |
| gross_profit_factor | 0.8212 |
| gross_win_rate | 0.4295 |
| sharpe_ratio | -10.5351 |
| sortino_ratio | -5.9513 |
| max_drawdown | 0.9994 |
| cagr | -0.9464 |
| net_avg_win | 15.2639 |
| net_avg_loss | -21.7240 |
| avg_hold_time_bars | 3.7722 |
| exposure | 0.2762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
