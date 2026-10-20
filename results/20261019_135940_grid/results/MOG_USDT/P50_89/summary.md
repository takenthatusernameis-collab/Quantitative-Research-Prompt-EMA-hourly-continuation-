# EMA Hourly Continuation — MOG/USDT P50_89

**Symbol:** MOG/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 592 |
| net_profit_factor | 0.6207 |
| net_win_rate | 0.4713 |
| gross_profit_factor | 0.9092 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -4.2106 |
| sortino_ratio | -1.5207 |
| max_drawdown | 0.8100 |
| cagr | -0.5095 |
| net_avg_win | 47.2324 |
| net_avg_loss | -67.8265 |
| avg_hold_time_bars | 4.4003 |
| exposure | 0.1295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
