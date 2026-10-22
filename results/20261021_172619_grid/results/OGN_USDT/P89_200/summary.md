# EMA Hourly Continuation — OGN/USDT P89_200

**Symbol:** OGN/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.5995 |
| net_win_rate | 0.4515 |
| gross_profit_factor | 0.7962 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -2.7065 |
| sortino_ratio | -0.6959 |
| max_drawdown | 0.5921 |
| cagr | -0.2748 |
| net_avg_win | 55.7823 |
| net_avg_loss | -76.6008 |
| avg_hold_time_bars | 13.2909 |
| exposure | 0.1985 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
