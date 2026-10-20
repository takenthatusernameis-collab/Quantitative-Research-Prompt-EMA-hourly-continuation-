# EMA Hourly Continuation — BABYDOGE/USDT P12_89

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 80 |
| net_profit_factor | 0.9754 |
| net_win_rate | 0.5125 |
| gross_profit_factor | 1.0411 |
| gross_win_rate | 0.5125 |
| sharpe_ratio | -0.0423 |
| sortino_ratio | -0.0054 |
| max_drawdown | 0.0669 |
| cagr | -0.0040 |
| net_avg_win | 96.4017 |
| net_avg_loss | -103.9035 |
| avg_hold_time_bars | 48.3500 |
| exposure | 0.1750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
