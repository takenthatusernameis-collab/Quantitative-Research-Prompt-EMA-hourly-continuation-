# EMA Hourly Continuation — FET/USDT P89_200

**Symbol:** FET/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 218 |
| net_profit_factor | 0.8205 |
| net_win_rate | 0.4954 |
| gross_profit_factor | 0.9810 |
| gross_win_rate | 0.4954 |
| sharpe_ratio | -0.9175 |
| sortino_ratio | -0.1938 |
| max_drawdown | 0.2424 |
| cagr | -0.0861 |
| net_avg_win | 85.6093 |
| net_avg_loss | -102.4409 |
| avg_hold_time_bars | 19.4266 |
| exposure | 0.1925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
