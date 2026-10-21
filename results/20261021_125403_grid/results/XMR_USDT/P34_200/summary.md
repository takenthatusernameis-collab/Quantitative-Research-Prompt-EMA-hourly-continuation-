# EMA Hourly Continuation — XMR/USDT P34_200

**Symbol:** XMR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.7572 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 0.9663 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -1.6973 |
| sortino_ratio | -0.4617 |
| max_drawdown | 0.4837 |
| cagr | -0.1913 |
| net_avg_win | 72.8273 |
| net_avg_loss | -92.0212 |
| avg_hold_time_bars | 25.7265 |
| exposure | 0.4233 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
