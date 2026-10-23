# EMA Hourly Continuation — CARV/USDT P26_55

**Symbol:** CARV/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.5075 |
| net_win_rate | 0.4633 |
| gross_profit_factor | 0.9162 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -5.5929 |
| sortino_ratio | -2.1981 |
| max_drawdown | 0.8849 |
| cagr | -0.6511 |
| net_avg_win | 31.3401 |
| net_avg_loss | -53.2951 |
| avg_hold_time_bars | 5.8962 |
| exposure | 0.2077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
