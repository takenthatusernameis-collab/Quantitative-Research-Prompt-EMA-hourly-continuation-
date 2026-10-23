# EMA Hourly Continuation — SKL/USDT P26_34

**Symbol:** SKL/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1151 |
| net_profit_factor | 0.2494 |
| net_win_rate | 0.3840 |
| gross_profit_factor | 0.6328 |
| gross_win_rate | 0.4335 |
| sharpe_ratio | -12.4677 |
| sortino_ratio | -6.0749 |
| max_drawdown | 0.9996 |
| cagr | -0.9571 |
| net_avg_win | 7.5151 |
| net_avg_loss | -18.7842 |
| avg_hold_time_bars | 2.1347 |
| exposure | 0.1117 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
