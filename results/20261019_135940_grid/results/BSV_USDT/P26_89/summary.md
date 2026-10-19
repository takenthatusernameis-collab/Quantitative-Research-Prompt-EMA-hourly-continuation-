# EMA Hourly Continuation — BSV/USDT P26_89

**Symbol:** BSV/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 778 |
| net_profit_factor | 0.4797 |
| net_win_rate | 0.4306 |
| gross_profit_factor | 0.8316 |
| gross_win_rate | 0.4460 |
| sharpe_ratio | -6.6927 |
| sortino_ratio | -2.6175 |
| max_drawdown | 0.9613 |
| cagr | -0.7228 |
| net_avg_win | 26.4257 |
| net_avg_loss | -41.6568 |
| avg_hold_time_bars | 9.5141 |
| exposure | 0.3365 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
