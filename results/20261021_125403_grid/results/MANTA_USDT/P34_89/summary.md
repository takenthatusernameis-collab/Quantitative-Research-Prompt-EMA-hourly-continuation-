# EMA Hourly Continuation — MANTA/USDT P34_89

**Symbol:** MANTA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.6979 |
| net_win_rate | 0.4644 |
| gross_profit_factor | 0.8900 |
| gross_win_rate | 0.4644 |
| sharpe_ratio | -2.6649 |
| sortino_ratio | -0.8050 |
| max_drawdown | 0.6281 |
| cagr | -0.3096 |
| net_avg_win | 66.9317 |
| net_avg_loss | -83.1726 |
| avg_hold_time_bars | 10.5600 |
| exposure | 0.2160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
