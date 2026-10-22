# EMA Hourly Continuation — ENA/USDT P26_200

**Symbol:** ENA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7920 |
| net_win_rate | 0.5053 |
| gross_profit_factor | 0.9936 |
| gross_win_rate | 0.5053 |
| sharpe_ratio | -1.3295 |
| sortino_ratio | -0.3642 |
| max_drawdown | 0.4265 |
| cagr | -0.1578 |
| net_avg_win | 70.5586 |
| net_avg_loss | -91.0171 |
| avg_hold_time_bars | 33.9064 |
| exposure | 0.5764 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
