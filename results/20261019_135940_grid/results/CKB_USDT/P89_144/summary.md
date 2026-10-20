# EMA Hourly Continuation — CKB/USDT P89_144

**Symbol:** CKB/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.4559 |
| net_win_rate | 0.4419 |
| gross_profit_factor | 0.7635 |
| gross_win_rate | 0.4494 |
| sharpe_ratio | -5.4150 |
| sortino_ratio | -1.7648 |
| max_drawdown | 0.8883 |
| cagr | -0.5792 |
| net_avg_win | 31.4664 |
| net_avg_loss | -54.6607 |
| avg_hold_time_bars | 5.3539 |
| exposure | 0.1300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
