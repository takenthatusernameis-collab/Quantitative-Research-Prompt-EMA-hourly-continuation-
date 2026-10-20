# EMA Hourly Continuation — BLUR/USDT P20_89

**Symbol:** BLUR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 699 |
| net_profit_factor | 0.6506 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 0.9704 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -4.1044 |
| sortino_ratio | -1.5288 |
| max_drawdown | 0.8560 |
| cagr | -0.5165 |
| net_avg_win | 47.1174 |
| net_avg_loss | -65.5156 |
| avg_hold_time_bars | 12.9428 |
| exposure | 0.4094 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
