# EMA Hourly Continuation — DEGEN/USDT P26_34

**Symbol:** DEGEN/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1003 |
| net_profit_factor | 0.4557 |
| net_win_rate | 0.4227 |
| gross_profit_factor | 0.8124 |
| gross_win_rate | 0.4437 |
| sharpe_ratio | -9.4327 |
| sortino_ratio | -4.2008 |
| max_drawdown | 0.9956 |
| cagr | -0.8841 |
| net_avg_win | 19.6535 |
| net_avg_loss | -31.5855 |
| avg_hold_time_bars | 2.4586 |
| exposure | 0.1123 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
