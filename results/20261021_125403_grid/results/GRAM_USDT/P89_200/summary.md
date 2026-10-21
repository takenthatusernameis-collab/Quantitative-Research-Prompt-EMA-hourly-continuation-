# EMA Hourly Continuation — GRAM/USDT P89_200

**Symbol:** GRAM/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.6714 |
| net_win_rate | 0.4819 |
| gross_profit_factor | 0.9096 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -1.9430 |
| sortino_ratio | -0.4616 |
| max_drawdown | 0.4422 |
| cagr | -0.1907 |
| net_avg_win | 63.3057 |
| net_avg_loss | -87.7020 |
| avg_hold_time_bars | 15.0652 |
| exposure | 0.1890 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
