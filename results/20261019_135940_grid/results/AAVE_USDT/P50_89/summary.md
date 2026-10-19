# EMA Hourly Continuation — AAVE/USDT P50_89

**Symbol:** AAVE/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.4670 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 0.8847 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -5.6792 |
| sortino_ratio | -2.1273 |
| max_drawdown | 0.9346 |
| cagr | -0.6479 |
| net_avg_win | 24.4768 |
| net_avg_loss | -46.8986 |
| avg_hold_time_bars | 4.1735 |
| exposure | 0.1334 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
