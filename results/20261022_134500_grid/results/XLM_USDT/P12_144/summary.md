# EMA Hourly Continuation — XLM/USDT P12_144

**Symbol:** XLM/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 553 |
| net_profit_factor | 0.4990 |
| net_win_rate | 0.4575 |
| gross_profit_factor | 0.8760 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -4.5194 |
| sortino_ratio | -1.4716 |
| max_drawdown | 0.8517 |
| cagr | -0.5215 |
| net_avg_win | 33.1855 |
| net_avg_loss | -56.0831 |
| avg_hold_time_bars | 26.0687 |
| exposure | 0.6553 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
