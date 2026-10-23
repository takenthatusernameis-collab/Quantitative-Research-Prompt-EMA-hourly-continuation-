# EMA Hourly Continuation — PUFFER/USDT P20_89

**Symbol:** PUFFER/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 522 |
| net_profit_factor | 0.7827 |
| net_win_rate | 0.5192 |
| gross_profit_factor | 1.0976 |
| gross_win_rate | 0.5249 |
| sharpe_ratio | -1.8809 |
| sortino_ratio | -0.6787 |
| max_drawdown | 0.4866 |
| cagr | -0.2767 |
| net_avg_win | 63.7754 |
| net_avg_loss | -87.9714 |
| avg_hold_time_bars | 14.0939 |
| exposure | 0.4163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
