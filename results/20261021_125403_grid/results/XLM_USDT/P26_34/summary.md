# EMA Hourly Continuation — XLM/USDT P26_34

**Symbol:** XLM/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 154 |
| net_profit_factor | 0.6749 |
| net_win_rate | 0.5065 |
| gross_profit_factor | 1.0275 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -1.5003 |
| sortino_ratio | -0.2683 |
| max_drawdown | 0.2829 |
| cagr | -0.1151 |
| net_avg_win | 70.3774 |
| net_avg_loss | -107.0243 |
| avg_hold_time_bars | 5.3312 |
| exposure | 0.0373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
