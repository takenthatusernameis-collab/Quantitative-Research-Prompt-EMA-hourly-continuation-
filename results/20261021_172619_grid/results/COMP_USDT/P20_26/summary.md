# EMA Hourly Continuation — COMP/USDT P20_26

**Symbol:** COMP/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.5397 |
| net_win_rate | 0.4618 |
| gross_profit_factor | 0.8496 |
| gross_win_rate | 0.4618 |
| sharpe_ratio | -3.1899 |
| sortino_ratio | -0.7605 |
| max_drawdown | 0.5921 |
| cagr | -0.2956 |
| net_avg_win | 54.0150 |
| net_avg_loss | -85.8902 |
| avg_hold_time_bars | 4.3673 |
| exposure | 0.0546 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
