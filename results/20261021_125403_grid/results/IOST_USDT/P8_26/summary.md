# EMA Hourly Continuation — IOST/USDT P8_26

**Symbol:** IOST/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 861 |
| net_profit_factor | 0.6528 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 0.9787 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -4.1772 |
| sortino_ratio | -1.7589 |
| max_drawdown | 0.8708 |
| cagr | -0.5539 |
| net_avg_win | 38.7717 |
| net_avg_loss | -56.8316 |
| avg_hold_time_bars | 6.4332 |
| exposure | 0.2518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
