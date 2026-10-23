# EMA Hourly Continuation — CFG/USDT P12_21

**Symbol:** CFG/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1555 |
| net_profit_factor | 0.2587 |
| net_win_rate | 0.3916 |
| gross_profit_factor | 0.6019 |
| gross_win_rate | 0.4071 |
| sharpe_ratio | -12.9588 |
| sortino_ratio | -7.2294 |
| max_drawdown | 0.9999 |
| cagr | -0.9741 |
| net_avg_win | 5.7302 |
| net_avg_loss | -14.2586 |
| avg_hold_time_bars | 2.3350 |
| exposure | 0.1650 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
