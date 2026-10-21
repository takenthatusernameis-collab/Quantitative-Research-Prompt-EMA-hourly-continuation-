# EMA Hourly Continuation — SEI/USDT P55_144

**Symbol:** SEI/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.7803 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9592 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -1.3465 |
| sortino_ratio | -0.3416 |
| max_drawdown | 0.3550 |
| cagr | -0.1463 |
| net_avg_win | 75.0893 |
| net_avg_loss | -93.2258 |
| avg_hold_time_bars | 17.2286 |
| exposure | 0.2467 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
