# EMA Hourly Continuation — BDX/USDT P55_144

**Symbol:** BDX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 987 |
| net_profit_factor | 0.2119 |
| net_win_rate | 0.2898 |
| gross_profit_factor | 0.5395 |
| gross_win_rate | 0.3485 |
| sharpe_ratio | -15.4041 |
| sortino_ratio | -7.1776 |
| max_drawdown | 1.0000 |
| cagr | -0.9815 |
| net_avg_win | 9.4016 |
| net_avg_loss | -18.1004 |
| avg_hold_time_bars | 5.2057 |
| exposure | 0.2335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
