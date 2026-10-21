# EMA Hourly Continuation — ATOM/USDT P20_50

**Symbol:** ATOM/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.6772 |
| net_win_rate | 0.4872 |
| gross_profit_factor | 0.9422 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -2.5893 |
| sortino_ratio | -0.8049 |
| max_drawdown | 0.6178 |
| cagr | -0.3082 |
| net_avg_win | 55.2959 |
| net_avg_loss | -77.5853 |
| avg_hold_time_bars | 7.9319 |
| exposure | 0.1695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
