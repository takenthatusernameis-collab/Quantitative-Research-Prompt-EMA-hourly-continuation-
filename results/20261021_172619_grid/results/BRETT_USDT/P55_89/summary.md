# EMA Hourly Continuation — BRETT/USDT P55_89

**Symbol:** BRETT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.7547 |
| net_win_rate | 0.4816 |
| gross_profit_factor | 0.9327 |
| gross_win_rate | 0.4816 |
| sharpe_ratio | -1.6148 |
| sortino_ratio | -0.4101 |
| max_drawdown | 0.3778 |
| cagr | -0.1721 |
| net_avg_win | 77.1544 |
| net_avg_loss | -94.9728 |
| avg_hold_time_bars | 6.0167 |
| exposure | 0.0866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
