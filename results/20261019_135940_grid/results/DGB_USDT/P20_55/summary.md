# EMA Hourly Continuation — DGB/USDT P20_55

**Symbol:** DGB/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1072 |
| net_profit_factor | 0.4637 |
| net_win_rate | 0.4338 |
| gross_profit_factor | 0.8609 |
| gross_win_rate | 0.4459 |
| sharpe_ratio | -8.5202 |
| sortino_ratio | -3.9103 |
| max_drawdown | 0.9930 |
| cagr | -0.8605 |
| net_avg_win | 18.4616 |
| net_avg_loss | -30.5000 |
| avg_hold_time_bars | 4.8125 |
| exposure | 0.2345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
