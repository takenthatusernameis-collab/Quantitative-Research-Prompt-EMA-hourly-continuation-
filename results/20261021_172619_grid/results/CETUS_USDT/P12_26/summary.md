# EMA Hourly Continuation — CETUS/USDT P12_26

**Symbol:** CETUS/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.7940 |
| net_win_rate | 0.5072 |
| gross_profit_factor | 1.0668 |
| gross_win_rate | 0.5072 |
| sharpe_ratio | -2.0231 |
| sortino_ratio | -0.6834 |
| max_drawdown | 0.5891 |
| cagr | -0.2700 |
| net_avg_win | 74.8720 |
| net_avg_loss | -97.0525 |
| avg_hold_time_bars | 4.9766 |
| exposure | 0.1252 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
