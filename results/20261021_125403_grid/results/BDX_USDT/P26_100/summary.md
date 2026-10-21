# EMA Hourly Continuation — BDX/USDT P26_100

**Symbol:** BDX/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.5402 |
| net_win_rate | 0.4534 |
| gross_profit_factor | 0.8483 |
| gross_win_rate | 0.4534 |
| sharpe_ratio | -4.0420 |
| sortino_ratio | -1.1683 |
| max_drawdown | 0.7566 |
| cagr | -0.4175 |
| net_avg_win | 47.1626 |
| net_avg_loss | -72.4291 |
| avg_hold_time_bars | 10.1152 |
| exposure | 0.1876 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
