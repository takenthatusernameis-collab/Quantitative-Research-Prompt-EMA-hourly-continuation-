# EMA Hourly Continuation — LUNC/USDT P55_89

**Symbol:** LUNC/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.8438 |
| net_win_rate | 0.5407 |
| gross_profit_factor | 1.1638 |
| gross_win_rate | 0.5407 |
| sharpe_ratio | -0.8121 |
| sortino_ratio | -0.1933 |
| max_drawdown | 0.2195 |
| cagr | -0.0858 |
| net_avg_win | 74.5961 |
| net_avg_loss | -104.0941 |
| avg_hold_time_bars | 7.1000 |
| exposure | 0.0871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
