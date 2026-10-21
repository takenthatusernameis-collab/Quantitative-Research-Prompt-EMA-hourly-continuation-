# EMA Hourly Continuation — ATOM/USDT P12_34

**Symbol:** ATOM/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.7546 |
| net_win_rate | 0.5139 |
| gross_profit_factor | 1.0660 |
| gross_win_rate | 0.5139 |
| sharpe_ratio | -2.1296 |
| sortino_ratio | -0.7138 |
| max_drawdown | 0.5824 |
| cagr | -0.2779 |
| net_avg_win | 61.7914 |
| net_avg_loss | -86.5517 |
| avg_hold_time_bars | 7.8392 |
| exposure | 0.1928 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
