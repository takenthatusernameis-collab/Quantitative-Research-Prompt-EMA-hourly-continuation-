# EMA Hourly Continuation — ILV/USDT P34_89

**Symbol:** ILV/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.8136 |
| net_win_rate | 0.5126 |
| gross_profit_factor | 1.0577 |
| gross_win_rate | 0.5126 |
| sharpe_ratio | -1.4330 |
| sortino_ratio | -0.4305 |
| max_drawdown | 0.4409 |
| cagr | -0.1802 |
| net_avg_win | 76.5292 |
| net_avg_loss | -98.9259 |
| avg_hold_time_bars | 12.0160 |
| exposure | 0.2387 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
