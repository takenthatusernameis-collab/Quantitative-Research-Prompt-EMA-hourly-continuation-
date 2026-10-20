# EMA Hourly Continuation — ZETA/USDT P55_144

**Symbol:** ZETA/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.5870 |
| net_win_rate | 0.4383 |
| gross_profit_factor | 0.8828 |
| gross_win_rate | 0.4547 |
| sharpe_ratio | -4.2070 |
| sortino_ratio | -1.3020 |
| max_drawdown | 0.8067 |
| cagr | -0.4615 |
| net_avg_win | 52.7313 |
| net_avg_loss | -70.0840 |
| avg_hold_time_bars | 12.4362 |
| exposure | 0.2735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
