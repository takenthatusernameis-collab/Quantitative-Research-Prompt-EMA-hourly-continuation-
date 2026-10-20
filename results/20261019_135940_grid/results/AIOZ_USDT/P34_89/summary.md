# EMA Hourly Continuation — AIOZ/USDT P34_89

**Symbol:** AIOZ/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 750 |
| net_profit_factor | 0.6024 |
| net_win_rate | 0.4480 |
| gross_profit_factor | 0.8939 |
| gross_win_rate | 0.4547 |
| sharpe_ratio | -5.4709 |
| sortino_ratio | -2.1175 |
| max_drawdown | 0.9205 |
| cagr | -0.6351 |
| net_avg_win | 41.5090 |
| net_avg_loss | -55.9229 |
| avg_hold_time_bars | 7.7760 |
| exposure | 0.2651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
