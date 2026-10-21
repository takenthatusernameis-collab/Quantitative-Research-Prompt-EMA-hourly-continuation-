# EMA Hourly Continuation — POPCAT/USDT P26_89

**Symbol:** POPCAT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.7508 |
| net_win_rate | 0.4734 |
| gross_profit_factor | 0.9037 |
| gross_win_rate | 0.4734 |
| sharpe_ratio | -2.0716 |
| sortino_ratio | -0.6466 |
| max_drawdown | 0.4752 |
| cagr | -0.2580 |
| net_avg_win | 73.0618 |
| net_avg_loss | -87.4883 |
| avg_hold_time_bars | 13.4179 |
| exposure | 0.2934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
