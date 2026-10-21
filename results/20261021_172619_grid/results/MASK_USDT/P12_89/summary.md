# EMA Hourly Continuation — MASK/USDT P12_89

**Symbol:** MASK/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.5698 |
| net_win_rate | 0.4452 |
| gross_profit_factor | 0.7710 |
| gross_win_rate | 0.4488 |
| sharpe_ratio | -3.8322 |
| sortino_ratio | -1.2821 |
| max_drawdown | 0.7823 |
| cagr | -0.4479 |
| net_avg_win | 41.4005 |
| net_avg_loss | -58.3098 |
| avg_hold_time_bars | 21.8043 |
| exposure | 0.5520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
