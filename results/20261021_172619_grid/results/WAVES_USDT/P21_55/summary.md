# EMA Hourly Continuation — WAVES/USDT P21_55

**Symbol:** WAVES/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.5379 |
| net_win_rate | 0.4280 |
| gross_profit_factor | 0.7589 |
| gross_win_rate | 0.4280 |
| sharpe_ratio | -4.7359 |
| sortino_ratio | -1.5595 |
| max_drawdown | 0.8430 |
| cagr | -0.5157 |
| net_avg_win | 42.6043 |
| net_avg_loss | -59.2716 |
| avg_hold_time_bars | 7.9981 |
| exposure | 0.1945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
