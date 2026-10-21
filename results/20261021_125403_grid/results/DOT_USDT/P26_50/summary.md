# EMA Hourly Continuation — DOT/USDT P26_50

**Symbol:** DOT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.8299 |
| net_win_rate | 0.5420 |
| gross_profit_factor | 1.1732 |
| gross_win_rate | 0.5420 |
| sharpe_ratio | -1.0649 |
| sortino_ratio | -0.2966 |
| max_drawdown | 0.3278 |
| cagr | -0.1274 |
| net_avg_win | 70.6958 |
| net_avg_loss | -100.8095 |
| avg_hold_time_bars | 6.5881 |
| exposure | 0.1105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
