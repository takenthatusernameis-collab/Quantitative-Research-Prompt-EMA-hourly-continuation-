# EMA Hourly Continuation — MANTA/USDT P55_144

**Symbol:** MANTA/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.6408 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.9176 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -3.0577 |
| sortino_ratio | -0.9600 |
| max_drawdown | 0.6778 |
| cagr | -0.3591 |
| net_avg_win | 51.7355 |
| net_avg_loss | -73.4558 |
| avg_hold_time_bars | 11.8522 |
| exposure | 0.2624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
