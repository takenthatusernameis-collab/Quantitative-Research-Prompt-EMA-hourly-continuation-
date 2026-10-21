# EMA Hourly Continuation — CGPT/USDT P34_144

**Symbol:** CGPT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.8657 |
| net_win_rate | 0.5060 |
| gross_profit_factor | 1.0332 |
| gross_win_rate | 0.5060 |
| sharpe_ratio | -0.8834 |
| sortino_ratio | -0.2322 |
| max_drawdown | 0.3363 |
| cagr | -0.1035 |
| net_avg_win | 91.0389 |
| net_avg_loss | -107.6902 |
| avg_hold_time_bars | 24.4732 |
| exposure | 0.3738 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
