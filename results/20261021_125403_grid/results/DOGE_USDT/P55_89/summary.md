# EMA Hourly Continuation — DOGE/USDT P55_89

**Symbol:** DOGE/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 261 |
| net_profit_factor | 0.7016 |
| net_win_rate | 0.5019 |
| gross_profit_factor | 0.9873 |
| gross_win_rate | 0.5019 |
| sharpe_ratio | -1.7089 |
| sortino_ratio | -0.3968 |
| max_drawdown | 0.3657 |
| cagr | -0.1658 |
| net_avg_win | 65.6493 |
| net_avg_loss | -94.2848 |
| avg_hold_time_bars | 7.2835 |
| exposure | 0.0864 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
