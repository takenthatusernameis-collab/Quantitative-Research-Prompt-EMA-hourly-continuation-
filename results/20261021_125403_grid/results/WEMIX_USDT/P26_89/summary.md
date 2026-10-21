# EMA Hourly Continuation — WEMIX/USDT P26_89

**Symbol:** WEMIX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.4982 |
| net_win_rate | 0.3787 |
| gross_profit_factor | 0.6389 |
| gross_win_rate | 0.3787 |
| sharpe_ratio | -4.7097 |
| sortino_ratio | -1.3363 |
| max_drawdown | 0.7938 |
| cagr | -0.4629 |
| net_avg_win | 51.2783 |
| net_avg_loss | -62.7349 |
| avg_hold_time_bars | 18.3144 |
| exposure | 0.3363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
