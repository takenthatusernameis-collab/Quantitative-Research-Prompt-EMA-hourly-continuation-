# EMA Hourly Continuation — CATI/USDT P8_144

**Symbol:** CATI/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.5397 |
| net_win_rate | 0.4217 |
| gross_profit_factor | 0.8009 |
| gross_win_rate | 0.4330 |
| sharpe_ratio | -4.5536 |
| sortino_ratio | -1.3105 |
| max_drawdown | 0.7757 |
| cagr | -0.4720 |
| net_avg_win | 58.2655 |
| net_avg_loss | -78.7124 |
| avg_hold_time_bars | 40.5442 |
| exposure | 0.7801 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
