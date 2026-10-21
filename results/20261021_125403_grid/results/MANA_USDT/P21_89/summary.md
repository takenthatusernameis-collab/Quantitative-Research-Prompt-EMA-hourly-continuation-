# EMA Hourly Continuation — MANA/USDT P21_89

**Symbol:** MANA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.7787 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 0.9990 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -2.0508 |
| sortino_ratio | -0.6434 |
| max_drawdown | 0.5792 |
| cagr | -0.2562 |
| net_avg_win | 78.1893 |
| net_avg_loss | -96.3329 |
| avg_hold_time_bars | 16.1618 |
| exposure | 0.3541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
