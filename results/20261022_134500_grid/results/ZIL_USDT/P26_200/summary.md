# EMA Hourly Continuation — ZIL/USDT P26_200

**Symbol:** ZIL/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.6856 |
| net_win_rate | 0.4987 |
| gross_profit_factor | 1.0306 |
| gross_win_rate | 0.5117 |
| sharpe_ratio | -2.1576 |
| sortino_ratio | -0.5960 |
| max_drawdown | 0.5445 |
| cagr | -0.2490 |
| net_avg_win | 58.2333 |
| net_avg_loss | -84.4991 |
| avg_hold_time_bars | 32.6260 |
| exposure | 0.5710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
