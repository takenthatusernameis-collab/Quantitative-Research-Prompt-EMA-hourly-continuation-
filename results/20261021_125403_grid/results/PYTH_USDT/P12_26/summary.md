# EMA Hourly Continuation — PYTH/USDT P12_26

**Symbol:** PYTH/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.7778 |
| net_win_rate | 0.5034 |
| gross_profit_factor | 1.0224 |
| gross_win_rate | 0.5034 |
| sharpe_ratio | -1.7319 |
| sortino_ratio | -0.5194 |
| max_drawdown | 0.4591 |
| cagr | -0.2124 |
| net_avg_win | 71.7495 |
| net_avg_loss | -93.5245 |
| avg_hold_time_bars | 5.2288 |
| exposure | 0.1039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
