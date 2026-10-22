# EMA Hourly Continuation — FIDA/USDT P26_144

**Symbol:** FIDA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.7197 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9054 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -2.0069 |
| sortino_ratio | -0.5863 |
| max_drawdown | 0.5126 |
| cagr | -0.2376 |
| net_avg_win | 62.6834 |
| net_avg_loss | -80.3664 |
| avg_hold_time_bars | 23.7660 |
| exposure | 0.4549 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
