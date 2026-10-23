# EMA Hourly Continuation — SUSHI/USDT P12_100

**Symbol:** SUSHI/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 606 |
| net_profit_factor | 0.5520 |
| net_win_rate | 0.4290 |
| gross_profit_factor | 0.8148 |
| gross_win_rate | 0.4389 |
| sharpe_ratio | -4.9991 |
| sortino_ratio | -1.7109 |
| max_drawdown | 0.8804 |
| cagr | -0.5680 |
| net_avg_win | 41.6855 |
| net_avg_loss | -56.7467 |
| avg_hold_time_bars | 21.8317 |
| exposure | 0.5987 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
