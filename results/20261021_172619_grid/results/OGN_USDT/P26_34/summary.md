# EMA Hourly Continuation — OGN/USDT P26_34

**Symbol:** OGN/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.5348 |
| net_win_rate | 0.4517 |
| gross_profit_factor | 0.8678 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -3.5214 |
| sortino_ratio | -0.8596 |
| max_drawdown | 0.6584 |
| cagr | -0.3281 |
| net_avg_win | 55.5746 |
| net_avg_loss | -85.6114 |
| avg_hold_time_bars | 5.8310 |
| exposure | 0.0765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
