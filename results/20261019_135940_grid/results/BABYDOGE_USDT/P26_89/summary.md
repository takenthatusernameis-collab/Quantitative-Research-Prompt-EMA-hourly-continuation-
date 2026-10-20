# EMA Hourly Continuation — BABYDOGE/USDT P26_89

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 46 |
| net_profit_factor | 1.2989 |
| net_win_rate | 0.5870 |
| gross_profit_factor | 1.4058 |
| gross_win_rate | 0.5870 |
| sharpe_ratio | 0.5769 |
| sortino_ratio | 0.0577 |
| max_drawdown | 0.0614 |
| cagr | 0.0239 |
| net_avg_win | 98.9843 |
| net_avg_loss | -108.2966 |
| avg_hold_time_bars | 34.0435 |
| exposure | 0.0709 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
