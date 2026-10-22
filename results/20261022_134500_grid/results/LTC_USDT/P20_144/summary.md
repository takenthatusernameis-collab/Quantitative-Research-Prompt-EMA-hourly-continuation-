# EMA Hourly Continuation — LTC/USDT P20_144

**Symbol:** LTC/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.3698 |
| net_win_rate | 0.4150 |
| gross_profit_factor | 0.7242 |
| gross_win_rate | 0.4407 |
| sharpe_ratio | -5.8533 |
| sortino_ratio | -1.8448 |
| max_drawdown | 0.9033 |
| cagr | -0.5993 |
| net_avg_win | 25.1360 |
| net_avg_loss | -48.2183 |
| avg_hold_time_bars | 23.3794 |
| exposure | 0.5377 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
