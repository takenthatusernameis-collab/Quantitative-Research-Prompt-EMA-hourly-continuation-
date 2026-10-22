# EMA Hourly Continuation — BAT/USDT P55_144

**Symbol:** BAT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.4928 |
| net_win_rate | 0.4506 |
| gross_profit_factor | 0.8655 |
| gross_win_rate | 0.4664 |
| sharpe_ratio | -4.4498 |
| sortino_ratio | -1.4145 |
| max_drawdown | 0.8183 |
| cagr | -0.4899 |
| net_avg_win | 34.7576 |
| net_avg_loss | -57.8419 |
| avg_hold_time_bars | 9.5040 |
| exposure | 0.2186 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
