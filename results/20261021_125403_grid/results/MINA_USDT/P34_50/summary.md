# EMA Hourly Continuation — MINA/USDT P34_50

**Symbol:** MINA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.7525 |
| net_win_rate | 0.5273 |
| gross_profit_factor | 1.1280 |
| gross_win_rate | 0.5273 |
| sharpe_ratio | -1.6935 |
| sortino_ratio | -0.4434 |
| max_drawdown | 0.4258 |
| cagr | -0.1843 |
| net_avg_win | 69.9637 |
| net_avg_loss | -103.7023 |
| avg_hold_time_bars | 5.2545 |
| exposure | 0.0788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
