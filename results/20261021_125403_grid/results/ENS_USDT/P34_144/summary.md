# EMA Hourly Continuation — ENS/USDT P34_144

**Symbol:** ENS/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.7803 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 0.9695 |
| gross_win_rate | 0.4958 |
| sharpe_ratio | -1.3817 |
| sortino_ratio | -0.3725 |
| max_drawdown | 0.3775 |
| cagr | -0.1583 |
| net_avg_win | 70.9072 |
| net_avg_loss | -89.3437 |
| avg_hold_time_bars | 24.7521 |
| exposure | 0.3994 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
