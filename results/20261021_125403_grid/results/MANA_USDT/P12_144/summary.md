# EMA Hourly Continuation — MANA/USDT P12_144

**Symbol:** MANA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.8453 |
| net_win_rate | 0.5092 |
| gross_profit_factor | 1.0173 |
| gross_win_rate | 0.5092 |
| sharpe_ratio | -0.7967 |
| sortino_ratio | -0.1885 |
| max_drawdown | 0.2204 |
| cagr | -0.0851 |
| net_avg_win | 78.6727 |
| net_avg_loss | -96.5469 |
| avg_hold_time_bars | 58.8828 |
| exposure | 0.7307 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
