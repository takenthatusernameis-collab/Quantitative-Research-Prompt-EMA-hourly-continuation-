# EMA Hourly Continuation — ARB/USDT P55_144

**Symbol:** ARB/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.8017 |
| net_win_rate | 0.5030 |
| gross_profit_factor | 1.0012 |
| gross_win_rate | 0.5030 |
| sharpe_ratio | -1.1997 |
| sortino_ratio | -0.3124 |
| max_drawdown | 0.3605 |
| cagr | -0.1348 |
| net_avg_win | 74.2117 |
| net_avg_loss | -93.7016 |
| avg_hold_time_bars | 14.5242 |
| exposure | 0.2179 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
