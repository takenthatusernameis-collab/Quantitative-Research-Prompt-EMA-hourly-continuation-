# EMA Hourly Continuation — KMNO/USDT P12_55

**Symbol:** KMNO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 858 |
| net_profit_factor | 0.6152 |
| net_win_rate | 0.4662 |
| gross_profit_factor | 0.9154 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -5.1519 |
| sortino_ratio | -2.1359 |
| max_drawdown | 0.9215 |
| cagr | -0.6428 |
| net_avg_win | 36.8373 |
| net_avg_loss | -52.2935 |
| avg_hold_time_bars | 9.4837 |
| exposure | 0.3757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
