# EMA Hourly Continuation — WOO/USDT P26_100

**Symbol:** WOO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 623 |
| net_profit_factor | 0.6938 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 1.0064 |
| gross_win_rate | 0.4864 |
| sharpe_ratio | -3.4417 |
| sortino_ratio | -1.2179 |
| max_drawdown | 0.7842 |
| cagr | -0.4349 |
| net_avg_win | 57.9100 |
| net_avg_loss | -76.5292 |
| avg_hold_time_bars | 12.9133 |
| exposure | 0.3657 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
