# EMA Hourly Continuation — POL/USDT P12_200

**Symbol:** POL/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.9738 |
| net_win_rate | 0.5409 |
| gross_profit_factor | 1.1682 |
| gross_win_rate | 0.5409 |
| sharpe_ratio | -0.0799 |
| sortino_ratio | -0.0186 |
| max_drawdown | 0.1808 |
| cagr | -0.0131 |
| net_avg_win | 86.9953 |
| net_avg_loss | -105.2326 |
| avg_hold_time_bars | 65.8210 |
| exposure | 0.7689 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
