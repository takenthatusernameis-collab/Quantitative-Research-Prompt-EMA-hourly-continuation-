# EMA Hourly Continuation — ENJ/USDT P26_200

**Symbol:** ENJ/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.7504 |
| net_win_rate | 0.5067 |
| gross_profit_factor | 1.0692 |
| gross_win_rate | 0.5121 |
| sharpe_ratio | -1.8502 |
| sortino_ratio | -0.5029 |
| max_drawdown | 0.4980 |
| cagr | -0.2144 |
| net_avg_win | 72.5348 |
| net_avg_loss | -99.2865 |
| avg_hold_time_bars | 34.9517 |
| exposure | 0.5899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
