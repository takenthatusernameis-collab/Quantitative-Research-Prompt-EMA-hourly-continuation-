# EMA Hourly Continuation — ORBS/USDT P20_89

**Symbol:** ORBS/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 757 |
| net_profit_factor | 0.5829 |
| net_win_rate | 0.4452 |
| gross_profit_factor | 0.9843 |
| gross_win_rate | 0.4584 |
| sharpe_ratio | -6.0972 |
| sortino_ratio | -2.3593 |
| max_drawdown | 0.9483 |
| cagr | -0.6844 |
| net_avg_win | 39.1775 |
| net_avg_loss | -53.9300 |
| avg_hold_time_bars | 12.8732 |
| exposure | 0.4430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
