# EMA Hourly Continuation — PEOPLE/USDT P21_89

**Symbol:** PEOPLE/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.7463 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9080 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -1.8985 |
| sortino_ratio | -0.5875 |
| max_drawdown | 0.5288 |
| cagr | -0.2365 |
| net_avg_win | 63.7085 |
| net_avg_loss | -79.4391 |
| avg_hold_time_bars | 18.7696 |
| exposure | 0.4017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
