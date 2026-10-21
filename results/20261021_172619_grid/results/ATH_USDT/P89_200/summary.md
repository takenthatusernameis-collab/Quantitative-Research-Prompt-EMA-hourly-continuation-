# EMA Hourly Continuation — ATH/USDT P89_200

**Symbol:** ATH/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.8008 |
| net_win_rate | 0.4925 |
| gross_profit_factor | 0.9719 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -1.1960 |
| sortino_ratio | -0.2890 |
| max_drawdown | 0.2995 |
| cagr | -0.1254 |
| net_avg_win | 82.4010 |
| net_avg_loss | -99.8742 |
| avg_hold_time_bars | 14.7313 |
| exposure | 0.1914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
