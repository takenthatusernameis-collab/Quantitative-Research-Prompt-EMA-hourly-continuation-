# EMA Hourly Continuation — CARV/USDT P20_34

**Symbol:** CARV/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 803 |
| net_profit_factor | 0.4147 |
| net_win_rate | 0.4471 |
| gross_profit_factor | 0.9045 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -8.0665 |
| sortino_ratio | -3.5831 |
| max_drawdown | 0.9740 |
| cagr | -0.8335 |
| net_avg_win | 19.2124 |
| net_avg_loss | -37.4637 |
| avg_hold_time_bars | 4.2291 |
| exposure | 0.1911 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
