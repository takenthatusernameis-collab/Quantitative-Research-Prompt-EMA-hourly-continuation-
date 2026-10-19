# EMA Hourly Continuation — VET/USDT P50_89

**Symbol:** VET/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.5320 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 1.0195 |
| gross_win_rate | 0.5089 |
| sharpe_ratio | -5.0811 |
| sortino_ratio | -1.8696 |
| max_drawdown | 0.8999 |
| cagr | -0.5940 |
| net_avg_win | 30.8692 |
| net_avg_loss | -55.6610 |
| avg_hold_time_bars | 4.5312 |
| exposure | 0.1388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
