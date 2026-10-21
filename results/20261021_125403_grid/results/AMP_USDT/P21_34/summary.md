# EMA Hourly Continuation — AMP/USDT P21_34

**Symbol:** AMP/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.3740 |
| net_win_rate | 0.3471 |
| gross_profit_factor | 0.5557 |
| gross_win_rate | 0.3471 |
| sharpe_ratio | -5.9376 |
| sortino_ratio | -1.6175 |
| max_drawdown | 0.8536 |
| cagr | -0.5301 |
| net_avg_win | 40.2992 |
| net_avg_loss | -57.2865 |
| avg_hold_time_bars | 5.2424 |
| exposure | 0.0865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
