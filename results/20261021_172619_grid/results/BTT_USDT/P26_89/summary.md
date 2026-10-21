# EMA Hourly Continuation — BTT/USDT P26_89

**Symbol:** BTT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.5123 |
| net_win_rate | 0.4189 |
| gross_profit_factor | 0.8119 |
| gross_win_rate | 0.4213 |
| sharpe_ratio | -5.2363 |
| sortino_ratio | -1.5254 |
| max_drawdown | 0.8413 |
| cagr | -0.5154 |
| net_avg_win | 50.8672 |
| net_avg_loss | -71.5778 |
| avg_hold_time_bars | 18.3753 |
| exposure | 0.3450 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
