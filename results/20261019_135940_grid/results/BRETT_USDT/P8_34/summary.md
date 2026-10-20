# EMA Hourly Continuation — BRETT/USDT P8_34

**Symbol:** BRETT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1317 |
| net_profit_factor | 0.5659 |
| net_win_rate | 0.4601 |
| gross_profit_factor | 0.8397 |
| gross_win_rate | 0.4685 |
| sharpe_ratio | -6.6226 |
| sortino_ratio | -3.4682 |
| max_drawdown | 0.9812 |
| cagr | -0.8122 |
| net_avg_win | 21.1067 |
| net_avg_loss | -31.7884 |
| avg_hold_time_bars | 5.4556 |
| exposure | 0.3457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
