# EMA Hourly Continuation — RENDER/USDT P26_89

**Symbol:** RENDER/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 615 |
| net_profit_factor | 0.6637 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9803 |
| gross_win_rate | 0.4927 |
| sharpe_ratio | -3.7163 |
| sortino_ratio | -1.3952 |
| max_drawdown | 0.7856 |
| cagr | -0.4876 |
| net_avg_win | 50.1384 |
| net_avg_loss | -72.4110 |
| avg_hold_time_bars | 9.0488 |
| exposure | 0.2937 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
