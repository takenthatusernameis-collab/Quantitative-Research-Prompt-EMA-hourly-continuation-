# EMA Hourly Continuation — AVAX/USDT P8_144

**Symbol:** AVAX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.6080 |
| net_win_rate | 0.4700 |
| gross_profit_factor | 0.9092 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -3.3522 |
| sortino_ratio | -1.0186 |
| max_drawdown | 0.7240 |
| cagr | -0.3855 |
| net_avg_win | 49.9660 |
| net_avg_loss | -72.8701 |
| avg_hold_time_bars | 34.7167 |
| exposure | 0.7354 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
