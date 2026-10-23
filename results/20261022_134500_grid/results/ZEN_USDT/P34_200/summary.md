# EMA Hourly Continuation — ZEN/USDT P34_200

**Symbol:** ZEN/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.7074 |
| net_win_rate | 0.4858 |
| gross_profit_factor | 0.9847 |
| gross_win_rate | 0.4976 |
| sharpe_ratio | -2.2128 |
| sortino_ratio | -0.6470 |
| max_drawdown | 0.5610 |
| cagr | -0.2602 |
| net_avg_win | 62.3097 |
| net_avg_loss | -83.2303 |
| avg_hold_time_bars | 26.9764 |
| exposure | 0.5199 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
