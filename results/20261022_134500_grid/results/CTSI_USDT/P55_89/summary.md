# EMA Hourly Continuation — CTSI/USDT P55_89

**Symbol:** CTSI/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 716 |
| net_profit_factor | 0.4584 |
| net_win_rate | 0.4497 |
| gross_profit_factor | 0.8584 |
| gross_win_rate | 0.4637 |
| sharpe_ratio | -6.2494 |
| sortino_ratio | -2.3618 |
| max_drawdown | 0.9446 |
| cagr | -0.6835 |
| net_avg_win | 24.8206 |
| net_avg_loss | -44.2539 |
| avg_hold_time_bars | 4.4735 |
| exposure | 0.1456 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
