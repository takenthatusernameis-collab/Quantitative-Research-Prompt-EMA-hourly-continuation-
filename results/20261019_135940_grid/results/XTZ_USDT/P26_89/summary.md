# EMA Hourly Continuation — XTZ/USDT P26_89

**Symbol:** XTZ/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.5853 |
| net_win_rate | 0.4699 |
| gross_profit_factor | 1.0053 |
| gross_win_rate | 0.4853 |
| sharpe_ratio | -4.9451 |
| sortino_ratio | -1.8662 |
| max_drawdown | 0.8985 |
| cagr | -0.5921 |
| net_avg_win | 37.5786 |
| net_avg_loss | -56.9244 |
| avg_hold_time_bars | 10.4601 |
| exposure | 0.3400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
