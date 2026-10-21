# EMA Hourly Continuation — CFG/USDT P34_89

**Symbol:** CFG/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.8010 |
| net_win_rate | 0.4989 |
| gross_profit_factor | 0.9904 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -1.4006 |
| sortino_ratio | -0.4239 |
| max_drawdown | 0.4698 |
| cagr | -0.1784 |
| net_avg_win | 70.3095 |
| net_avg_loss | -87.3802 |
| avg_hold_time_bars | 9.8993 |
| exposure | 0.2011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
