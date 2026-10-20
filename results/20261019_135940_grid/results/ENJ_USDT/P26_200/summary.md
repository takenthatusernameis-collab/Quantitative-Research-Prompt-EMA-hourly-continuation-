# EMA Hourly Continuation — ENJ/USDT P26_200

**Symbol:** ENJ/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.7300 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0264 |
| gross_win_rate | 0.5054 |
| sharpe_ratio | -1.9859 |
| sortino_ratio | -0.5388 |
| max_drawdown | 0.4980 |
| cagr | -0.2270 |
| net_avg_win | 69.9558 |
| net_avg_loss | -95.8335 |
| avg_hold_time_bars | 35.2880 |
| exposure | 0.5903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
