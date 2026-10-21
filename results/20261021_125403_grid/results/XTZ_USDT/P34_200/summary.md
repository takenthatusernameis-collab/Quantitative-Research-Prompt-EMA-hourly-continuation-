# EMA Hourly Continuation — XTZ/USDT P34_200

**Symbol:** XTZ/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.7626 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 0.9736 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -1.4918 |
| sortino_ratio | -0.3841 |
| max_drawdown | 0.3763 |
| cagr | -0.1620 |
| net_avg_win | 71.9545 |
| net_avg_loss | -92.0494 |
| avg_hold_time_bars | 34.0216 |
| exposure | 0.5010 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
