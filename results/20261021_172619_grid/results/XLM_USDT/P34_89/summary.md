# EMA Hourly Continuation — XLM/USDT P34_89

**Symbol:** XLM/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.7144 |
| net_win_rate | 0.5061 |
| gross_profit_factor | 1.0206 |
| gross_win_rate | 0.5061 |
| sharpe_ratio | -2.0094 |
| sortino_ratio | -0.5845 |
| max_drawdown | 0.4997 |
| cagr | -0.2337 |
| net_avg_win | 58.9211 |
| net_avg_loss | -84.5136 |
| avg_hold_time_bars | 12.4743 |
| exposure | 0.2319 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
