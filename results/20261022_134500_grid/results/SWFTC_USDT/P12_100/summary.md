# EMA Hourly Continuation — SWFTC/USDT P12_100

**Symbol:** SWFTC/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 821 |
| net_profit_factor | 0.5151 |
| net_win_rate | 0.4129 |
| gross_profit_factor | 0.7836 |
| gross_win_rate | 0.4227 |
| sharpe_ratio | -6.7191 |
| sortino_ratio | -2.7007 |
| max_drawdown | 0.9636 |
| cagr | -0.7309 |
| net_avg_win | 30.1800 |
| net_avg_loss | -41.2050 |
| avg_hold_time_bars | 12.7734 |
| exposure | 0.4767 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
