# EMA Hourly Continuation — AUCTION/USDT P20_100

**Symbol:** AUCTION/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.6312 |
| net_win_rate | 0.4523 |
| gross_profit_factor | 0.8378 |
| gross_win_rate | 0.4561 |
| sharpe_ratio | -3.5000 |
| sortino_ratio | -1.1300 |
| max_drawdown | 0.7495 |
| cagr | -0.4106 |
| net_avg_win | 53.1903 |
| net_avg_loss | -69.5841 |
| avg_hold_time_bars | 18.1107 |
| exposure | 0.4295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
