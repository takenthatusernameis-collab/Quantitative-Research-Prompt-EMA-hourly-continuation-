# EMA Hourly Continuation — ARKM/USDT P26_89

**Symbol:** ARKM/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 740 |
| net_profit_factor | 0.5825 |
| net_win_rate | 0.4581 |
| gross_profit_factor | 0.8740 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -4.6959 |
| sortino_ratio | -1.8051 |
| max_drawdown | 0.8848 |
| cagr | -0.5732 |
| net_avg_win | 36.3076 |
| net_avg_loss | -52.6917 |
| avg_hold_time_bars | 8.8757 |
| exposure | 0.2985 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
