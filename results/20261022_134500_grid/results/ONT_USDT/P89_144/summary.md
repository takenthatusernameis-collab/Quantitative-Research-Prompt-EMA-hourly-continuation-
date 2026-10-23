# EMA Hourly Continuation — ONT/USDT P89_144

**Symbol:** ONT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.4724 |
| net_win_rate | 0.4623 |
| gross_profit_factor | 0.8748 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -4.6651 |
| sortino_ratio | -1.4479 |
| max_drawdown | 0.8327 |
| cagr | -0.5078 |
| net_avg_win | 32.8501 |
| net_avg_loss | -59.7881 |
| avg_hold_time_bars | 5.6049 |
| exposure | 0.1245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
