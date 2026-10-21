# EMA Hourly Continuation — DEGEN/USDT P50_89

**Symbol:** DEGEN/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.7626 |
| net_win_rate | 0.4877 |
| gross_profit_factor | 0.9517 |
| gross_win_rate | 0.4877 |
| sharpe_ratio | -1.6732 |
| sortino_ratio | -0.4570 |
| max_drawdown | 0.4256 |
| cagr | -0.1895 |
| net_avg_win | 73.9155 |
| net_avg_loss | -92.2597 |
| avg_hold_time_bars | 7.7014 |
| exposure | 0.1280 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
