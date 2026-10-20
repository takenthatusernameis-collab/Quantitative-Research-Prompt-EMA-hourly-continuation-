# EMA Hourly Continuation — G/USDT P89_200

**Symbol:** G/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.5632 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.8929 |
| gross_win_rate | 0.4727 |
| sharpe_ratio | -3.5012 |
| sortino_ratio | -0.9653 |
| max_drawdown | 0.6470 |
| cagr | -0.3686 |
| net_avg_win | 52.8740 |
| net_avg_loss | -82.1398 |
| avg_hold_time_bars | 11.5333 |
| exposure | 0.2001 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
