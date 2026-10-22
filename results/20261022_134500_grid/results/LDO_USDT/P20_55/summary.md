# EMA Hourly Continuation — LDO/USDT P20_55

**Symbol:** LDO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1014 |
| net_profit_factor | 0.4820 |
| net_win_rate | 0.4428 |
| gross_profit_factor | 0.8116 |
| gross_win_rate | 0.4527 |
| sharpe_ratio | -7.2908 |
| sortino_ratio | -3.2538 |
| max_drawdown | 0.9820 |
| cagr | -0.7981 |
| net_avg_win | 20.3541 |
| net_avg_loss | -33.5558 |
| avg_hold_time_bars | 4.9359 |
| exposure | 0.2275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
