# EMA Hourly Continuation — CELO/USDT P21_89

**Symbol:** CELO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.8098 |
| net_win_rate | 0.5031 |
| gross_profit_factor | 1.0141 |
| gross_win_rate | 0.5031 |
| sharpe_ratio | -1.4540 |
| sortino_ratio | -0.4570 |
| max_drawdown | 0.4385 |
| cagr | -0.1908 |
| net_avg_win | 72.4963 |
| net_avg_loss | -90.6427 |
| avg_hold_time_bars | 18.2816 |
| exposure | 0.3996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
