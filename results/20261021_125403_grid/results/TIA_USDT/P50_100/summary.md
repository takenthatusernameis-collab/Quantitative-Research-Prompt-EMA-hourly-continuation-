# EMA Hourly Continuation — TIA/USDT P50_100

**Symbol:** TIA/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.8787 |
| net_win_rate | 0.5226 |
| gross_profit_factor | 1.0855 |
| gross_win_rate | 0.5226 |
| sharpe_ratio | -0.7112 |
| sortino_ratio | -0.1928 |
| max_drawdown | 0.2060 |
| cagr | -0.0875 |
| net_avg_win | 80.3709 |
| net_avg_loss | -100.1303 |
| avg_hold_time_bars | 9.5989 |
| exposure | 0.1545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
