# EMA Hourly Continuation — EWT/USDT P34_144

**Symbol:** EWT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 539 |
| net_profit_factor | 0.5211 |
| net_win_rate | 0.4434 |
| gross_profit_factor | 0.7569 |
| gross_win_rate | 0.4471 |
| sharpe_ratio | -4.1950 |
| sortino_ratio | -1.3618 |
| max_drawdown | 0.8291 |
| cagr | -0.4820 |
| net_avg_win | 36.8057 |
| net_avg_loss | -56.2657 |
| avg_hold_time_bars | 12.1521 |
| exposure | 0.2977 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
