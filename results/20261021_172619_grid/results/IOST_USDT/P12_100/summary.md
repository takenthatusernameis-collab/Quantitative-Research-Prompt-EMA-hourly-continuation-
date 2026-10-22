# EMA Hourly Continuation — IOST/USDT P12_100

**Symbol:** IOST/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.8688 |
| net_win_rate | 0.5283 |
| gross_profit_factor | 1.1142 |
| gross_win_rate | 0.5283 |
| sharpe_ratio | -0.9345 |
| sortino_ratio | -0.2826 |
| max_drawdown | 0.3855 |
| cagr | -0.1249 |
| net_avg_win | 80.8818 |
| net_avg_loss | -104.2913 |
| avg_hold_time_bars | 30.7846 |
| exposure | 0.6171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
