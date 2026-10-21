# EMA Hourly Continuation — SKL/USDT P8_100

**Symbol:** SKL/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.8141 |
| net_win_rate | 0.4947 |
| gross_profit_factor | 0.9745 |
| gross_win_rate | 0.4947 |
| sharpe_ratio | -1.4370 |
| sortino_ratio | -0.4463 |
| max_drawdown | 0.4741 |
| cagr | -0.1872 |
| net_avg_win | 75.9237 |
| net_avg_loss | -91.3152 |
| avg_hold_time_bars | 31.7717 |
| exposure | 0.6831 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
