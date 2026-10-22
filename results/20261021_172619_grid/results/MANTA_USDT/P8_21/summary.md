# EMA Hourly Continuation — MANTA/USDT P8_21

**Symbol:** MANTA/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.7623 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 1.0304 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -2.6313 |
| sortino_ratio | -0.9559 |
| max_drawdown | 0.6816 |
| cagr | -0.3545 |
| net_avg_win | 66.8239 |
| net_avg_loss | -87.1197 |
| avg_hold_time_bars | 5.6075 |
| exposure | 0.1636 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
