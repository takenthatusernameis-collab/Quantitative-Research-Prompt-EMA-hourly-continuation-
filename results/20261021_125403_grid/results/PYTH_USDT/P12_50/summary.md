# EMA Hourly Continuation — PYTH/USDT P12_50

**Symbol:** PYTH/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.8003 |
| net_win_rate | 0.4943 |
| gross_profit_factor | 0.9833 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -1.8079 |
| sortino_ratio | -0.6402 |
| max_drawdown | 0.5723 |
| cagr | -0.2562 |
| net_avg_win | 69.3631 |
| net_avg_loss | -84.7136 |
| avg_hold_time_bars | 11.0962 |
| exposure | 0.3092 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
