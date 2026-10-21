# EMA Hourly Continuation — DEGEN/USDT P55_144

**Symbol:** DEGEN/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.9777 |
| net_win_rate | 0.5409 |
| gross_profit_factor | 1.1692 |
| gross_win_rate | 0.5409 |
| sharpe_ratio | -0.0877 |
| sortino_ratio | -0.0235 |
| max_drawdown | 0.2415 |
| cagr | -0.0169 |
| net_avg_win | 99.1527 |
| net_avg_loss | -119.5066 |
| avg_hold_time_bars | 15.8129 |
| exposure | 0.2462 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
