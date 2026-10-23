# EMA Hourly Continuation — API3/USDT P20_200

**Symbol:** API3/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.6801 |
| net_win_rate | 0.4785 |
| gross_profit_factor | 0.9351 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -2.5909 |
| sortino_ratio | -0.7393 |
| max_drawdown | 0.6126 |
| cagr | -0.3002 |
| net_avg_win | 62.9329 |
| net_avg_loss | -84.8943 |
| avg_hold_time_bars | 32.9617 |
| exposure | 0.6263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
