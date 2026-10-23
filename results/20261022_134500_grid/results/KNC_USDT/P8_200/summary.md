# EMA Hourly Continuation — KNC/USDT P8_200

**Symbol:** KNC/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.6300 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.8850 |
| gross_win_rate | 0.4732 |
| sharpe_ratio | -2.4056 |
| sortino_ratio | -0.5878 |
| max_drawdown | 0.5211 |
| cagr | -0.2394 |
| net_avg_win | 61.3224 |
| net_avg_loss | -83.9519 |
| avg_hold_time_bars | 62.5738 |
| exposure | 0.8476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
