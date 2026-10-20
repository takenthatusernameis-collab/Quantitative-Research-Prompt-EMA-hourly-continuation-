# EMA Hourly Continuation — CARV/USDT P8_55

**Symbol:** CARV/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 749 |
| net_profit_factor | 0.6763 |
| net_win_rate | 0.4967 |
| gross_profit_factor | 1.0920 |
| gross_win_rate | 0.5127 |
| sharpe_ratio | -4.1217 |
| sortino_ratio | -1.7606 |
| max_drawdown | 0.8288 |
| cagr | -0.5714 |
| net_avg_win | 46.0814 |
| net_avg_loss | -67.2381 |
| avg_hold_time_bars | 12.0574 |
| exposure | 0.5082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
