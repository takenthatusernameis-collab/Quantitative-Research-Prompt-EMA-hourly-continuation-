# EMA Hourly Continuation — EGLD/USDT P12_89

**Symbol:** EGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.8659 |
| net_win_rate | 0.5228 |
| gross_profit_factor | 1.0952 |
| gross_win_rate | 0.5228 |
| sharpe_ratio | -1.0362 |
| sortino_ratio | -0.3353 |
| max_drawdown | 0.4487 |
| cagr | -0.1458 |
| net_avg_win | 79.9378 |
| net_avg_loss | -101.1247 |
| avg_hold_time_bars | 24.0851 |
| exposure | 0.5529 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
