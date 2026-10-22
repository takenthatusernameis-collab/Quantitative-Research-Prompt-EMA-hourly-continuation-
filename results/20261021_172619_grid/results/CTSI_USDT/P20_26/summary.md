# EMA Hourly Continuation — CTSI/USDT P20_26

**Symbol:** CTSI/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.4593 |
| net_win_rate | 0.4000 |
| gross_profit_factor | 0.7044 |
| gross_win_rate | 0.4000 |
| sharpe_ratio | -4.7466 |
| sortino_ratio | -1.2618 |
| max_drawdown | 0.7687 |
| cagr | -0.4418 |
| net_avg_win | 47.3152 |
| net_avg_loss | -68.6793 |
| avg_hold_time_bars | 5.7507 |
| exposure | 0.0902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
