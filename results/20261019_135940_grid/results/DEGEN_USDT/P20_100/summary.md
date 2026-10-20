# EMA Hourly Continuation — DEGEN/USDT P20_100

**Symbol:** DEGEN/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 668 |
| net_profit_factor | 0.7256 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 0.9708 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -3.2487 |
| sortino_ratio | -1.1831 |
| max_drawdown | 0.7853 |
| cagr | -0.4314 |
| net_avg_win | 62.7564 |
| net_avg_loss | -79.0588 |
| avg_hold_time_bars | 13.8787 |
| exposure | 0.4221 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
