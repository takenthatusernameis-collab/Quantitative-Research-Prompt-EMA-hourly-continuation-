# EMA Hourly Continuation — TNSR/USDT P12_26

**Symbol:** TNSR/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 561 |
| net_profit_factor | 0.7787 |
| net_win_rate | 0.5098 |
| gross_profit_factor | 1.0652 |
| gross_win_rate | 0.5116 |
| sharpe_ratio | -2.1362 |
| sortino_ratio | -0.7254 |
| max_drawdown | 0.6082 |
| cagr | -0.2831 |
| net_avg_win | 69.8888 |
| net_avg_loss | -93.3429 |
| avg_hold_time_bars | 5.0303 |
| exposure | 0.1277 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
