# EMA Hourly Continuation — SAFE/USDT P26_89

**Symbol:** SAFE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 673 |
| net_profit_factor | 0.6242 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9798 |
| gross_win_rate | 0.4889 |
| sharpe_ratio | -3.9732 |
| sortino_ratio | -1.4545 |
| max_drawdown | 0.8434 |
| cagr | -0.5053 |
| net_avg_win | 42.5282 |
| net_avg_loss | -62.8761 |
| avg_hold_time_bars | 11.0119 |
| exposure | 0.3394 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
