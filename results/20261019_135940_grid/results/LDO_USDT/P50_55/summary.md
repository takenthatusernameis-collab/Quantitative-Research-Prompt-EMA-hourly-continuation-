# EMA Hourly Continuation — LDO/USDT P50_55

**Symbol:** LDO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 923 |
| net_profit_factor | 0.2265 |
| net_win_rate | 0.3413 |
| gross_profit_factor | 0.6391 |
| gross_win_rate | 0.3857 |
| sharpe_ratio | -13.2652 |
| sortino_ratio | -5.9090 |
| max_drawdown | 0.9997 |
| cagr | -0.9581 |
| net_avg_win | 9.2932 |
| net_avg_loss | -21.2564 |
| avg_hold_time_bars | 1.7768 |
| exposure | 0.0745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
