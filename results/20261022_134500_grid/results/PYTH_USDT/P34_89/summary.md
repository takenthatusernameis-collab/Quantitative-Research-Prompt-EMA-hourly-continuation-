# EMA Hourly Continuation — PYTH/USDT P34_89

**Symbol:** PYTH/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.5733 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.8925 |
| gross_win_rate | 0.4739 |
| sharpe_ratio | -4.6480 |
| sortino_ratio | -1.7512 |
| max_drawdown | 0.8788 |
| cagr | -0.5625 |
| net_avg_win | 35.3928 |
| net_avg_loss | -54.3671 |
| avg_hold_time_bars | 7.1396 |
| exposure | 0.2301 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
