# EMA Hourly Continuation — BONK/USDT P21_144

**Symbol:** BONK/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.6531 |
| net_win_rate | 0.4722 |
| gross_profit_factor | 0.8918 |
| gross_win_rate | 0.4786 |
| sharpe_ratio | -2.9618 |
| sortino_ratio | -0.8967 |
| max_drawdown | 0.7255 |
| cagr | -0.3517 |
| net_avg_win | 56.5116 |
| net_avg_loss | -77.4156 |
| avg_hold_time_bars | 26.6752 |
| exposure | 0.5675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
