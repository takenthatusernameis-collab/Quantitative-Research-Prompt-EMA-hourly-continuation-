# EMA Hourly Continuation — GTC/USDT P55_200

**Symbol:** GTC/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.6608 |
| net_win_rate | 0.4526 |
| gross_profit_factor | 0.8148 |
| gross_win_rate | 0.4526 |
| sharpe_ratio | -2.2776 |
| sortino_ratio | -0.5837 |
| max_drawdown | 0.5073 |
| cagr | -0.2357 |
| net_avg_win | 64.6263 |
| net_avg_loss | -80.8589 |
| avg_hold_time_bars | 25.0612 |
| exposure | 0.3725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
