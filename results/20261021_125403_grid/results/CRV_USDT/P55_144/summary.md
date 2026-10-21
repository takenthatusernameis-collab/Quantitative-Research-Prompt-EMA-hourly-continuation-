# EMA Hourly Continuation — CRV/USDT P55_144

**Symbol:** CRV/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.8203 |
| net_win_rate | 0.5071 |
| gross_profit_factor | 1.0262 |
| gross_win_rate | 0.5071 |
| sharpe_ratio | -1.1565 |
| sortino_ratio | -0.3110 |
| max_drawdown | 0.3084 |
| cagr | -0.1343 |
| net_avg_win | 77.9040 |
| net_avg_loss | -97.7180 |
| avg_hold_time_bars | 13.2080 |
| exposure | 0.2107 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
