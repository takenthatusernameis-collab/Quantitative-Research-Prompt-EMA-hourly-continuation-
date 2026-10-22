# EMA Hourly Continuation — MANA/USDT P26_100

**Symbol:** MANA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.6333 |
| net_win_rate | 0.4613 |
| gross_profit_factor | 1.0381 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -5.0244 |
| sortino_ratio | -1.7916 |
| max_drawdown | 0.8988 |
| cagr | -0.5862 |
| net_avg_win | 51.6411 |
| net_avg_loss | -69.8241 |
| avg_hold_time_bars | 12.4690 |
| exposure | 0.3661 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
