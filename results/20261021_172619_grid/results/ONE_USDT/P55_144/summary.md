# EMA Hourly Continuation — ONE/USDT P55_144

**Symbol:** ONE/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.8401 |
| net_win_rate | 0.5061 |
| gross_profit_factor | 1.0339 |
| gross_win_rate | 0.5061 |
| sharpe_ratio | -1.0172 |
| sortino_ratio | -0.2636 |
| max_drawdown | 0.3110 |
| cagr | -0.1156 |
| net_avg_win | 84.5635 |
| net_avg_loss | -103.1568 |
| avg_hold_time_bars | 17.9356 |
| exposure | 0.2658 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
