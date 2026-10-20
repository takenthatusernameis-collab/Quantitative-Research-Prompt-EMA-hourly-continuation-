# EMA Hourly Continuation — REQ/USDT P55_89

**Symbol:** REQ/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 779 |
| net_profit_factor | 0.3838 |
| net_win_rate | 0.3800 |
| gross_profit_factor | 0.9496 |
| gross_win_rate | 0.4236 |
| sharpe_ratio | -10.2154 |
| sortino_ratio | -4.1028 |
| max_drawdown | 0.9950 |
| cagr | -0.8783 |
| net_avg_win | 20.9363 |
| net_avg_loss | -33.4300 |
| avg_hold_time_bars | 4.1733 |
| exposure | 0.1478 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
