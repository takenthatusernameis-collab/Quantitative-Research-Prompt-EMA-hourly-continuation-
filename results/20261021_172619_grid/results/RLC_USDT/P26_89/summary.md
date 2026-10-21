# EMA Hourly Continuation — RLC/USDT P26_89

**Symbol:** RLC/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.7929 |
| net_win_rate | 0.5125 |
| gross_profit_factor | 1.0409 |
| gross_win_rate | 0.5125 |
| sharpe_ratio | -1.6731 |
| sortino_ratio | -0.5483 |
| max_drawdown | 0.5254 |
| cagr | -0.2232 |
| net_avg_win | 67.3657 |
| net_avg_loss | -89.3053 |
| avg_hold_time_bars | 11.9367 |
| exposure | 0.2827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
