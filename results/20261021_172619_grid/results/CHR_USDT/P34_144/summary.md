# EMA Hourly Continuation — CHR/USDT P34_144

**Symbol:** CHR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.8030 |
| net_win_rate | 0.4949 |
| gross_profit_factor | 0.9779 |
| gross_win_rate | 0.4949 |
| sharpe_ratio | -1.3491 |
| sortino_ratio | -0.3822 |
| max_drawdown | 0.3909 |
| cagr | -0.1624 |
| net_avg_win | 75.3441 |
| net_avg_loss | -91.9472 |
| avg_hold_time_bars | 23.2640 |
| exposure | 0.4148 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
