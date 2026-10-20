# EMA Hourly Continuation — XNO/USDT P26_89

**Symbol:** XNO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 875 |
| net_profit_factor | 0.4847 |
| net_win_rate | 0.3977 |
| gross_profit_factor | 0.7787 |
| gross_win_rate | 0.4046 |
| sharpe_ratio | -7.9147 |
| sortino_ratio | -3.3022 |
| max_drawdown | 0.9821 |
| cagr | -0.7972 |
| net_avg_win | 26.5362 |
| net_avg_loss | -36.1531 |
| avg_hold_time_bars | 7.9897 |
| exposure | 0.3178 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
