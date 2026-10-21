# EMA Hourly Continuation — AMP/USDT P12_20

**Symbol:** AMP/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.3665 |
| net_win_rate | 0.3568 |
| gross_profit_factor | 0.5557 |
| gross_win_rate | 0.3568 |
| sharpe_ratio | -5.9316 |
| sortino_ratio | -1.6593 |
| max_drawdown | 0.8583 |
| cagr | -0.5373 |
| net_avg_win | 36.1348 |
| net_avg_loss | -54.6829 |
| avg_hold_time_bars | 4.5599 |
| exposure | 0.0796 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
