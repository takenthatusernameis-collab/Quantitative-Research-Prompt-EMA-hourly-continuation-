# EMA Hourly Continuation — BCH/USDT P55_200

**Symbol:** BCH/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.8264 |
| net_win_rate | 0.5166 |
| gross_profit_factor | 1.0671 |
| gross_win_rate | 0.5166 |
| sharpe_ratio | -0.9933 |
| sortino_ratio | -0.2350 |
| max_drawdown | 0.3029 |
| cagr | -0.1033 |
| net_avg_win | 81.4561 |
| net_avg_loss | -105.3389 |
| avg_hold_time_bars | 29.4539 |
| exposure | 0.3628 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
