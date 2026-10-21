# EMA Hourly Continuation — DASH/USDT P34_89

**Symbol:** DASH/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.7301 |
| net_win_rate | 0.4912 |
| gross_profit_factor | 0.9765 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -1.9734 |
| sortino_ratio | -0.5641 |
| max_drawdown | 0.5013 |
| cagr | -0.2280 |
| net_avg_win | 65.9602 |
| net_avg_loss | -87.2271 |
| avg_hold_time_bars | 11.8221 |
| exposure | 0.2144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
