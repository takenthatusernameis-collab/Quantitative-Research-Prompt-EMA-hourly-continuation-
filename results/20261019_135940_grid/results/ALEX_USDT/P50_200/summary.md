# EMA Hourly Continuation — ALEX/USDT P50_200

**Symbol:** ALEX/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.5405 |
| net_win_rate | 0.4012 |
| gross_profit_factor | 0.7278 |
| gross_win_rate | 0.4041 |
| sharpe_ratio | -3.9670 |
| sortino_ratio | -1.0220 |
| max_drawdown | 0.7234 |
| cagr | -0.3869 |
| net_avg_win | 61.1737 |
| net_avg_loss | -75.8266 |
| avg_hold_time_bars | 26.5900 |
| exposure | 0.4097 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
