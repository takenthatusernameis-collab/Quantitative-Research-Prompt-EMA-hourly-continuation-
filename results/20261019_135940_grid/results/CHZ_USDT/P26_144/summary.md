# EMA Hourly Continuation — CHZ/USDT P26_144

**Symbol:** CHZ/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.7304 |
| net_win_rate | 0.5171 |
| gross_profit_factor | 1.1160 |
| gross_win_rate | 0.5285 |
| sharpe_ratio | -2.0132 |
| sortino_ratio | -0.5914 |
| max_drawdown | 0.5278 |
| cagr | -0.2502 |
| net_avg_win | 61.4427 |
| net_avg_loss | -90.0693 |
| avg_hold_time_bars | 25.5968 |
| exposure | 0.5108 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
