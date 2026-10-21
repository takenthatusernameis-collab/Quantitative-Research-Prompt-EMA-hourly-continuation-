# EMA Hourly Continuation — SNX/USDT P8_89

**Symbol:** SNX/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 552 |
| net_profit_factor | 0.8070 |
| net_win_rate | 0.4928 |
| gross_profit_factor | 0.9798 |
| gross_win_rate | 0.4928 |
| sharpe_ratio | -1.6589 |
| sortino_ratio | -0.5558 |
| max_drawdown | 0.4949 |
| cagr | -0.2273 |
| net_avg_win | 73.5073 |
| net_avg_loss | -88.4839 |
| avg_hold_time_bars | 23.8859 |
| exposure | 0.5966 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
