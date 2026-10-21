# EMA Hourly Continuation — GRAM/USDT P55_89

**Symbol:** GRAM/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 261 |
| net_profit_factor | 0.7095 |
| net_win_rate | 0.5057 |
| gross_profit_factor | 1.0303 |
| gross_win_rate | 0.5057 |
| sharpe_ratio | -1.7532 |
| sortino_ratio | -0.4078 |
| max_drawdown | 0.4277 |
| cagr | -0.1698 |
| net_avg_win | 69.1035 |
| net_avg_loss | -99.6561 |
| avg_hold_time_bars | 7.3103 |
| exposure | 0.0867 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
