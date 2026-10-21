# EMA Hourly Continuation — JST/USDT P144_200

**Symbol:** JST/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 207 |
| net_profit_factor | 0.4962 |
| net_win_rate | 0.5072 |
| gross_profit_factor | 0.9931 |
| gross_win_rate | 0.5121 |
| sharpe_ratio | -2.7409 |
| sortino_ratio | -0.5681 |
| max_drawdown | 0.4965 |
| cagr | -0.2316 |
| net_avg_win | 45.5478 |
| net_avg_loss | -94.4867 |
| avg_hold_time_bars | 9.1594 |
| exposure | 0.0858 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
