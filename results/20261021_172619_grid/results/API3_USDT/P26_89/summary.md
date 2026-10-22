# EMA Hourly Continuation — API3/USDT P26_89

**Symbol:** API3/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.7711 |
| net_win_rate | 0.4968 |
| gross_profit_factor | 0.9756 |
| gross_win_rate | 0.4968 |
| sharpe_ratio | -1.7306 |
| sortino_ratio | -0.5389 |
| max_drawdown | 0.4964 |
| cagr | -0.2196 |
| net_avg_win | 66.4445 |
| net_avg_loss | -85.0841 |
| avg_hold_time_bars | 14.6829 |
| exposure | 0.3157 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
