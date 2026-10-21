# EMA Hourly Continuation — JST/USDT P55_200

**Symbol:** JST/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.7014 |
| net_win_rate | 0.5251 |
| gross_profit_factor | 1.0844 |
| gross_win_rate | 0.5284 |
| sharpe_ratio | -1.7080 |
| sortino_ratio | -0.4216 |
| max_drawdown | 0.4051 |
| cagr | -0.1781 |
| net_avg_win | 58.3936 |
| net_avg_loss | -92.0468 |
| avg_hold_time_bars | 27.5284 |
| exposure | 0.3725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
