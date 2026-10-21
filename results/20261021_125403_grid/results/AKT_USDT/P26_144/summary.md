# EMA Hourly Continuation — AKT/USDT P26_144

**Symbol:** AKT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.9001 |
| net_win_rate | 0.5157 |
| gross_profit_factor | 1.0580 |
| gross_win_rate | 0.5157 |
| sharpe_ratio | -0.6104 |
| sortino_ratio | -0.1714 |
| max_drawdown | 0.2070 |
| cagr | -0.0798 |
| net_avg_win | 86.1731 |
| net_avg_loss | -101.9460 |
| avg_hold_time_bars | 24.1099 |
| exposure | 0.4186 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
