# EMA Hourly Continuation — KAVA/USDT P34_89

**Symbol:** KAVA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.6317 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.9273 |
| gross_win_rate | 0.4671 |
| sharpe_ratio | -3.9306 |
| sortino_ratio | -1.2518 |
| max_drawdown | 0.7883 |
| cagr | -0.4447 |
| net_avg_win | 57.0621 |
| net_avg_loss | -77.9028 |
| avg_hold_time_bars | 10.6108 |
| exposure | 0.2416 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
