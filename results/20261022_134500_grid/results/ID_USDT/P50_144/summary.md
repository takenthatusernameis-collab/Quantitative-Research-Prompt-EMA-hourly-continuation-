# EMA Hourly Continuation — ID/USDT P50_144

**Symbol:** ID/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.6238 |
| net_win_rate | 0.4880 |
| gross_profit_factor | 0.9277 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -2.7809 |
| sortino_ratio | -0.8393 |
| max_drawdown | 0.6357 |
| cagr | -0.3269 |
| net_avg_win | 46.7556 |
| net_avg_loss | -71.4417 |
| avg_hold_time_bars | 13.9542 |
| exposure | 0.2899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
