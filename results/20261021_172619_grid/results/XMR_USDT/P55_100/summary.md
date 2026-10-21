# EMA Hourly Continuation — XMR/USDT P55_100

**Symbol:** XMR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.5114 |
| net_win_rate | 0.4191 |
| gross_profit_factor | 0.7214 |
| gross_win_rate | 0.4191 |
| sharpe_ratio | -3.3429 |
| sortino_ratio | -0.7842 |
| max_drawdown | 0.6006 |
| cagr | -0.3022 |
| net_avg_win | 54.6182 |
| net_avg_loss | -77.0641 |
| avg_hold_time_bars | 7.5993 |
| exposure | 0.0940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
