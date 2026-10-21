# EMA Hourly Continuation — ID/USDT P55_144

**Symbol:** ID/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.7179 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 0.9179 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -1.7929 |
| sortino_ratio | -0.4929 |
| max_drawdown | 0.4415 |
| cagr | -0.2026 |
| net_avg_win | 61.1595 |
| net_avg_loss | -80.7361 |
| avg_hold_time_bars | 14.4382 |
| exposure | 0.2431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
