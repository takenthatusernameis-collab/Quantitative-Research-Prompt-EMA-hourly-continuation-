# EMA Hourly Continuation — BRETT/USDT P8_89

**Symbol:** BRETT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.8542 |
| net_win_rate | 0.4968 |
| gross_profit_factor | 0.9825 |
| gross_win_rate | 0.4968 |
| sharpe_ratio | -1.0984 |
| sortino_ratio | -0.3499 |
| max_drawdown | 0.3690 |
| cagr | -0.1522 |
| net_avg_win | 81.4684 |
| net_avg_loss | -94.1669 |
| avg_hold_time_bars | 27.6119 |
| exposure | 0.6231 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
