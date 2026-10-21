# EMA Hourly Continuation — ATH/USDT P21_34

**Symbol:** ATH/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 234 |
| net_profit_factor | 0.8396 |
| net_win_rate | 0.5299 |
| gross_profit_factor | 1.1259 |
| gross_win_rate | 0.5299 |
| sharpe_ratio | -0.8613 |
| sortino_ratio | -0.1965 |
| max_drawdown | 0.2418 |
| cagr | -0.0871 |
| net_avg_win | 81.5240 |
| net_avg_loss | -109.4566 |
| avg_hold_time_bars | 4.5983 |
| exposure | 0.0522 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
