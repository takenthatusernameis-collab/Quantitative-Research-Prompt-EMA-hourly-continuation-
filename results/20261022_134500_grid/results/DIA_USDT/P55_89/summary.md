# EMA Hourly Continuation — DIA/USDT P55_89

**Symbol:** DIA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 697 |
| net_profit_factor | 0.5924 |
| net_win_rate | 0.4993 |
| gross_profit_factor | 1.0871 |
| gross_win_rate | 0.5151 |
| sharpe_ratio | -4.6518 |
| sortino_ratio | -1.7289 |
| max_drawdown | 0.8850 |
| cagr | -0.5667 |
| net_avg_win | 36.7010 |
| net_avg_loss | -61.7736 |
| avg_hold_time_bars | 4.3314 |
| exposure | 0.1366 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
