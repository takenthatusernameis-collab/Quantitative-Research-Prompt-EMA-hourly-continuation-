# EMA Hourly Continuation — DUSK/USDT P21_144

**Symbol:** DUSK/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.6820 |
| net_win_rate | 0.4819 |
| gross_profit_factor | 0.9360 |
| gross_win_rate | 0.4879 |
| sharpe_ratio | -2.4685 |
| sortino_ratio | -0.7791 |
| max_drawdown | 0.6147 |
| cagr | -0.3042 |
| net_avg_win | 53.6406 |
| net_avg_loss | -73.1460 |
| avg_hold_time_bars | 22.7762 |
| exposure | 0.5135 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
