# EMA Hourly Continuation — ARB/USDT P8_144

**Symbol:** ARB/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.9487 |
| net_win_rate | 0.5296 |
| gross_profit_factor | 1.1217 |
| gross_win_rate | 0.5296 |
| sharpe_ratio | -0.2339 |
| sortino_ratio | -0.0572 |
| max_drawdown | 0.1389 |
| cagr | -0.0302 |
| net_avg_win | 90.2373 |
| net_avg_loss | -107.0898 |
| avg_hold_time_bars | 60.9895 |
| exposure | 0.7956 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
