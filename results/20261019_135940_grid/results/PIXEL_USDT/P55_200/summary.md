# EMA Hourly Continuation — PIXEL/USDT P55_200

**Symbol:** PIXEL/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.7411 |
| net_win_rate | 0.4927 |
| gross_profit_factor | 0.9679 |
| gross_win_rate | 0.4927 |
| sharpe_ratio | -1.7560 |
| sortino_ratio | -0.4586 |
| max_drawdown | 0.4412 |
| cagr | -0.1943 |
| net_avg_win | 71.5856 |
| net_avg_loss | -93.8072 |
| avg_hold_time_bars | 27.3959 |
| exposure | 0.4227 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
