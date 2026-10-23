# EMA Hourly Continuation — DEGEN/USDT P20_144

**Symbol:** DEGEN/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.7781 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 1.0003 |
| gross_win_rate | 0.4950 |
| sharpe_ratio | -2.0827 |
| sortino_ratio | -0.6591 |
| max_drawdown | 0.6058 |
| cagr | -0.2696 |
| net_avg_win | 77.4029 |
| net_avg_loss | -96.7292 |
| avg_hold_time_bars | 24.0958 |
| exposure | 0.5496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
