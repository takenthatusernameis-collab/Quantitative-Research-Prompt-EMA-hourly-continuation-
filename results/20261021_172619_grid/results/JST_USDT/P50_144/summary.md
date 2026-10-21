# EMA Hourly Continuation — JST/USDT P50_144

**Symbol:** JST/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.6657 |
| net_win_rate | 0.5194 |
| gross_profit_factor | 1.0975 |
| gross_win_rate | 0.5284 |
| sharpe_ratio | -2.1179 |
| sortino_ratio | -0.5543 |
| max_drawdown | 0.4817 |
| cagr | -0.2259 |
| net_avg_win | 54.4630 |
| net_avg_loss | -88.4149 |
| avg_hold_time_bars | 19.3970 |
| exposure | 0.2940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
