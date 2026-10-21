# EMA Hourly Continuation — CPOOL/USDT P12_50

**Symbol:** CPOOL/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.8221 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 0.9888 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -1.6057 |
| sortino_ratio | -0.5835 |
| max_drawdown | 0.4982 |
| cagr | -0.2378 |
| net_avg_win | 71.1921 |
| net_avg_loss | -85.5270 |
| avg_hold_time_bars | 9.6966 |
| exposure | 0.2847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
