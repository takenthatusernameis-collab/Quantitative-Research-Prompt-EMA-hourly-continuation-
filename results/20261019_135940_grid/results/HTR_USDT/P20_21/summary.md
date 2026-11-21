# EMA Hourly Continuation — HTR/USDT P20_21

**Symbol:** HTR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1115 |
| net_profit_factor | 0.2029 |
| net_win_rate | 0.2610 |
| gross_profit_factor | 0.6054 |
| gross_win_rate | 0.3112 |
| sharpe_ratio | -16.8627 |
| sortino_ratio | -8.3239 |
| max_drawdown | 1.0000 |
| cagr | -0.9901 |
| net_avg_win | 8.7497 |
| net_avg_loss | -15.2258 |
| avg_hold_time_bars | 2.4646 |
| exposure | 0.1249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
