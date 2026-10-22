# EMA Hourly Continuation — PUFFER/USDT P20_144

**Symbol:** PUFFER/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 1.0484 |
| net_win_rate | 0.5511 |
| gross_profit_factor | 1.2210 |
| gross_win_rate | 0.5511 |
| sharpe_ratio | 0.3641 |
| sortino_ratio | 0.1061 |
| max_drawdown | 0.1418 |
| cagr | 0.0388 |
| net_avg_win | 97.1088 |
| net_avg_loss | -113.7034 |
| avg_hold_time_bars | 29.5882 |
| exposure | 0.5408 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
