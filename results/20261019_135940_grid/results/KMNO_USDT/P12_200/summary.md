# EMA Hourly Continuation — KMNO/USDT P12_200

**Symbol:** KMNO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.6907 |
| net_win_rate | 0.4640 |
| gross_profit_factor | 0.9227 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -2.4388 |
| sortino_ratio | -0.6424 |
| max_drawdown | 0.5861 |
| cagr | -0.2652 |
| net_avg_win | 73.9525 |
| net_avg_loss | -92.6758 |
| avg_hold_time_bars | 45.5620 |
| exposure | 0.7300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
