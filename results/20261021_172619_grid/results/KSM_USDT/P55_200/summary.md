# EMA Hourly Continuation — KSM/USDT P55_200

**Symbol:** KSM/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.8302 |
| net_win_rate | 0.5168 |
| gross_profit_factor | 1.0594 |
| gross_win_rate | 0.5168 |
| sharpe_ratio | -0.9666 |
| sortino_ratio | -0.2397 |
| max_drawdown | 0.2853 |
| cagr | -0.1060 |
| net_avg_win | 77.8344 |
| net_avg_loss | -100.2693 |
| avg_hold_time_bars | 26.3154 |
| exposure | 0.3565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
