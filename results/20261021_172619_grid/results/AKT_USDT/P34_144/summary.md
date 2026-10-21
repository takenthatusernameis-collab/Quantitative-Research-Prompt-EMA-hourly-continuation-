# EMA Hourly Continuation — AKT/USDT P34_144

**Symbol:** AKT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.8461 |
| net_win_rate | 0.5041 |
| gross_profit_factor | 1.0067 |
| gross_win_rate | 0.5041 |
| sharpe_ratio | -0.9519 |
| sortino_ratio | -0.2612 |
| max_drawdown | 0.2725 |
| cagr | -0.1158 |
| net_avg_win | 78.9852 |
| net_avg_loss | -94.8901 |
| avg_hold_time_bars | 20.9482 |
| exposure | 0.3495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
