# EMA Hourly Continuation — NEAR/USDT P50_144

**Symbol:** NEAR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.6266 |
| net_win_rate | 0.4787 |
| gross_profit_factor | 0.9347 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -3.0645 |
| sortino_ratio | -0.9294 |
| max_drawdown | 0.6873 |
| cagr | -0.3627 |
| net_avg_win | 50.5246 |
| net_avg_loss | -74.0491 |
| avg_hold_time_bars | 11.8255 |
| exposure | 0.2526 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
