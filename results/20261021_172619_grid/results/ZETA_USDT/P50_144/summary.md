# EMA Hourly Continuation — ZETA/USDT P50_144

**Symbol:** ZETA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.6713 |
| net_win_rate | 0.4502 |
| gross_profit_factor | 0.8326 |
| gross_win_rate | 0.4502 |
| sharpe_ratio | -2.3912 |
| sortino_ratio | -0.6156 |
| max_drawdown | 0.5376 |
| cagr | -0.2473 |
| net_avg_win | 70.1005 |
| net_avg_loss | -85.4965 |
| avg_hold_time_bars | 20.3051 |
| exposure | 0.3041 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
