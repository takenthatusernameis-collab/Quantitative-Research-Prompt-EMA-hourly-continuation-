# EMA Hourly Continuation — UNI/USDT P12_50

**Symbol:** UNI/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 568 |
| net_profit_factor | 0.8226 |
| net_win_rate | 0.5123 |
| gross_profit_factor | 1.0429 |
| gross_win_rate | 0.5123 |
| sharpe_ratio | -1.4128 |
| sortino_ratio | -0.4840 |
| max_drawdown | 0.4495 |
| cagr | -0.2010 |
| net_avg_win | 68.6646 |
| net_avg_loss | -87.6876 |
| avg_hold_time_bars | 10.9296 |
| exposure | 0.2822 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
