# EMA Hourly Continuation — CHR/USDT P20_89

**Symbol:** CHR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.7192 |
| net_win_rate | 0.4630 |
| gross_profit_factor | 0.8828 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -2.6032 |
| sortino_ratio | -0.8578 |
| max_drawdown | 0.6648 |
| cagr | -0.3266 |
| net_avg_win | 64.6617 |
| net_avg_loss | -77.5098 |
| avg_hold_time_bars | 15.5370 |
| exposure | 0.3797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
