# EMA Hourly Continuation — XLM/USDT P8_144

**Symbol:** XLM/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.8043 |
| net_win_rate | 0.5061 |
| gross_profit_factor | 1.0256 |
| gross_win_rate | 0.5086 |
| sharpe_ratio | -1.3246 |
| sortino_ratio | -0.3838 |
| max_drawdown | 0.3906 |
| cagr | -0.1631 |
| net_avg_win | 71.5796 |
| net_avg_loss | -91.1985 |
| avg_hold_time_bars | 38.2763 |
| exposure | 0.7116 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
