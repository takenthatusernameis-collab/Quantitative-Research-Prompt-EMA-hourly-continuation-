# EMA Hourly Continuation — ENS/USDT P55_144

**Symbol:** ENS/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.6943 |
| net_win_rate | 0.4716 |
| gross_profit_factor | 0.8806 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -2.0244 |
| sortino_ratio | -0.5277 |
| max_drawdown | 0.4783 |
| cagr | -0.2157 |
| net_avg_win | 65.6726 |
| net_avg_loss | -84.4297 |
| avg_hold_time_bars | 15.9463 |
| exposure | 0.2428 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
