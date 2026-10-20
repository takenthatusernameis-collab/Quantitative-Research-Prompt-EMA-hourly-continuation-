# EMA Hourly Continuation — DYDX/USDT P50_55

**Symbol:** DYDX/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 833 |
| net_profit_factor | 0.1754 |
| net_win_rate | 0.3589 |
| gross_profit_factor | 0.6514 |
| gross_win_rate | 0.4178 |
| sharpe_ratio | -11.8853 |
| sortino_ratio | -5.0372 |
| max_drawdown | 0.9987 |
| cagr | -0.9288 |
| net_avg_win | 7.1051 |
| net_avg_loss | -22.6804 |
| avg_hold_time_bars | 1.7935 |
| exposure | 0.0679 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
