# EMA Hourly Continuation — APT/USDT P55_89

**Symbol:** APT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 681 |
| net_profit_factor | 0.4771 |
| net_win_rate | 0.4640 |
| gross_profit_factor | 0.9127 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -5.8210 |
| sortino_ratio | -2.1497 |
| max_drawdown | 0.9312 |
| cagr | -0.6520 |
| net_avg_win | 26.8341 |
| net_avg_loss | -48.6952 |
| avg_hold_time_bars | 3.6344 |
| exposure | 0.1125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
