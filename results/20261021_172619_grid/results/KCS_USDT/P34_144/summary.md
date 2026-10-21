# EMA Hourly Continuation — KCS/USDT P34_144

**Symbol:** KCS/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.5706 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 0.9453 |
| gross_win_rate | 0.4802 |
| sharpe_ratio | -3.1546 |
| sortino_ratio | -0.8204 |
| max_drawdown | 0.6175 |
| cagr | -0.3131 |
| net_avg_win | 51.6890 |
| net_avg_loss | -82.6832 |
| avg_hold_time_bars | 27.1125 |
| exposure | 0.4055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
