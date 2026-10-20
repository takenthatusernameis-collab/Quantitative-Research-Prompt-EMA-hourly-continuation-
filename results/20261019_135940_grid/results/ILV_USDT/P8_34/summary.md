# EMA Hourly Continuation — ILV/USDT P8_34

**Symbol:** ILV/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1368 |
| net_profit_factor | 0.5298 |
| net_win_rate | 0.4642 |
| gross_profit_factor | 0.9163 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -7.7418 |
| sortino_ratio | -4.0096 |
| max_drawdown | 0.9932 |
| cagr | -0.8614 |
| net_avg_win | 17.6204 |
| net_avg_loss | -28.8116 |
| avg_hold_time_bars | 5.2003 |
| exposure | 0.3234 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
