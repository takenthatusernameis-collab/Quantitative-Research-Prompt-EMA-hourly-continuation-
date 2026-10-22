# EMA Hourly Continuation — POKT/USDT P26_89

**Symbol:** POKT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.6701 |
| net_win_rate | 0.4400 |
| gross_profit_factor | 0.8579 |
| gross_win_rate | 0.4400 |
| sharpe_ratio | -3.3706 |
| sortino_ratio | -1.0637 |
| max_drawdown | 0.7307 |
| cagr | -0.3883 |
| net_avg_win | 65.5957 |
| net_avg_loss | -76.9154 |
| avg_hold_time_bars | 13.5880 |
| exposure | 0.3074 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
