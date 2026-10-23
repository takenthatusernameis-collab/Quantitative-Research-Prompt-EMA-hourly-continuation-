# EMA Hourly Continuation — ASTR/USDT P8_55

**Symbol:** ASTR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 915 |
| net_profit_factor | 0.6548 |
| net_win_rate | 0.4973 |
| gross_profit_factor | 1.0736 |
| gross_win_rate | 0.5169 |
| sharpe_ratio | -4.2164 |
| sortino_ratio | -1.7977 |
| max_drawdown | 0.8881 |
| cagr | -0.5731 |
| net_avg_win | 36.8241 |
| net_avg_loss | -55.6231 |
| avg_hold_time_bars | 12.6918 |
| exposure | 0.5255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
