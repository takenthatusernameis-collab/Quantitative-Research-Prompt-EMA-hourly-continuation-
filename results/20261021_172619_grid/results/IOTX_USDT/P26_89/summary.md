# EMA Hourly Continuation — IOTX/USDT P26_89

**Symbol:** IOTX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.6989 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.9017 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -2.5512 |
| sortino_ratio | -0.7929 |
| max_drawdown | 0.6139 |
| cagr | -0.3047 |
| net_avg_win | 61.7539 |
| net_avg_loss | -79.5195 |
| avg_hold_time_bars | 13.5116 |
| exposure | 0.2917 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
