# EMA Hourly Continuation — DEEP/USDT P12_89

**Symbol:** DEEP/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.7455 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 0.9988 |
| gross_win_rate | 0.4954 |
| sharpe_ratio | -2.7273 |
| sortino_ratio | -0.9997 |
| max_drawdown | 0.6498 |
| cagr | -0.3785 |
| net_avg_win | 67.6446 |
| net_avg_loss | -88.4216 |
| avg_hold_time_bars | 18.1201 |
| exposure | 0.5550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
