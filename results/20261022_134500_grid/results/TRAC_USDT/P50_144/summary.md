# EMA Hourly Continuation — TRAC/USDT P50_144

**Symbol:** TRAC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 522 |
| net_profit_factor | 0.6618 |
| net_win_rate | 0.4962 |
| gross_profit_factor | 0.9638 |
| gross_win_rate | 0.4962 |
| sharpe_ratio | -2.8004 |
| sortino_ratio | -0.9020 |
| max_drawdown | 0.6643 |
| cagr | -0.3484 |
| net_avg_win | 49.7977 |
| net_avg_loss | -74.0969 |
| avg_hold_time_bars | 10.7490 |
| exposure | 0.2550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
