# EMA Hourly Continuation — NEAR/USDT P8_89

**Symbol:** NEAR/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 732 |
| net_profit_factor | 0.6634 |
| net_win_rate | 0.4740 |
| gross_profit_factor | 0.9521 |
| gross_win_rate | 0.4850 |
| sharpe_ratio | -3.7998 |
| sortino_ratio | -1.4414 |
| max_drawdown | 0.8311 |
| cagr | -0.4996 |
| net_avg_win | 46.8242 |
| net_avg_loss | -63.6110 |
| avg_hold_time_bars | 19.0943 |
| exposure | 0.6353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
