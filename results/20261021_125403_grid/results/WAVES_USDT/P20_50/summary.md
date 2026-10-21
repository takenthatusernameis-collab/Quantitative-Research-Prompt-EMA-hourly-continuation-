# EMA Hourly Continuation — WAVES/USDT P20_50

**Symbol:** WAVES/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.5714 |
| net_win_rate | 0.4316 |
| gross_profit_factor | 0.8139 |
| gross_win_rate | 0.4316 |
| sharpe_ratio | -4.6390 |
| sortino_ratio | -1.5154 |
| max_drawdown | 0.8307 |
| cagr | -0.5054 |
| net_avg_win | 48.6995 |
| net_avg_loss | -64.7083 |
| avg_hold_time_bars | 7.4848 |
| exposure | 0.1790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
