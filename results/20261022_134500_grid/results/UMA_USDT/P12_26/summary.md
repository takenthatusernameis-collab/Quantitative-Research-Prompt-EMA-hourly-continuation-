# EMA Hourly Continuation — UMA/USDT P12_26

**Symbol:** UMA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1298 |
| net_profit_factor | 0.3716 |
| net_win_rate | 0.4099 |
| gross_profit_factor | 0.7949 |
| gross_win_rate | 0.4291 |
| sharpe_ratio | -11.2134 |
| sortino_ratio | -5.7382 |
| max_drawdown | 0.9993 |
| cagr | -0.9437 |
| net_avg_win | 11.1060 |
| net_avg_loss | -20.7586 |
| avg_hold_time_bars | 3.4245 |
| exposure | 0.2020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
