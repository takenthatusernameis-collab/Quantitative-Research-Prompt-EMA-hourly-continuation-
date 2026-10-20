# EMA Hourly Continuation — EUL/USDT P20_100

**Symbol:** EUL/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.5001 |
| net_win_rate | 0.4450 |
| gross_profit_factor | 0.7325 |
| gross_win_rate | 0.4497 |
| sharpe_ratio | -4.5880 |
| sortino_ratio | -1.6280 |
| max_drawdown | 0.8638 |
| cagr | -0.5412 |
| net_avg_win | 30.3518 |
| net_avg_loss | -48.6580 |
| avg_hold_time_bars | 13.7799 |
| exposure | 0.3984 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
