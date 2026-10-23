# EMA Hourly Continuation — MANTA/USDT P34_100

**Symbol:** MANTA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 645 |
| net_profit_factor | 0.5644 |
| net_win_rate | 0.4496 |
| gross_profit_factor | 0.8506 |
| gross_win_rate | 0.4558 |
| sharpe_ratio | -4.6750 |
| sortino_ratio | -1.6720 |
| max_drawdown | 0.8683 |
| cagr | -0.5499 |
| net_avg_win | 38.6552 |
| net_avg_loss | -55.9525 |
| avg_hold_time_bars | 9.2946 |
| exposure | 0.2725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
