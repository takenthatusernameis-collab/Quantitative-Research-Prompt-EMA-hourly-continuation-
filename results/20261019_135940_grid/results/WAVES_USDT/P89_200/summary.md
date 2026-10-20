# EMA Hourly Continuation — WAVES/USDT P89_200

**Symbol:** WAVES/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.3883 |
| net_win_rate | 0.4060 |
| gross_profit_factor | 0.6851 |
| gross_win_rate | 0.4274 |
| sharpe_ratio | -5.8581 |
| sortino_ratio | -1.7823 |
| max_drawdown | 0.8958 |
| cagr | -0.5892 |
| net_avg_win | 29.8378 |
| net_avg_loss | -52.5127 |
| avg_hold_time_bars | 9.4316 |
| exposure | 0.2006 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
