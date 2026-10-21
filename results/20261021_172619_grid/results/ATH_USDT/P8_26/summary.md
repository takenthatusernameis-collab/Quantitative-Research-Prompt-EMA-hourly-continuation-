# EMA Hourly Continuation — ATH/USDT P8_26

**Symbol:** ATH/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.8709 |
| net_win_rate | 0.5322 |
| gross_profit_factor | 1.1316 |
| gross_win_rate | 0.5322 |
| sharpe_ratio | -1.0416 |
| sortino_ratio | -0.3776 |
| max_drawdown | 0.3881 |
| cagr | -0.1626 |
| net_avg_win | 73.3738 |
| net_avg_loss | -95.8539 |
| avg_hold_time_bars | 6.4475 |
| exposure | 0.1844 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
