# EMA Hourly Continuation — DGB/USDT P26_144

**Symbol:** DGB/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 599 |
| net_profit_factor | 0.6017 |
| net_win_rate | 0.4457 |
| gross_profit_factor | 0.8876 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -4.6455 |
| sortino_ratio | -1.5993 |
| max_drawdown | 0.8653 |
| cagr | -0.5354 |
| net_avg_win | 48.3280 |
| net_avg_loss | -64.5921 |
| avg_hold_time_bars | 17.3790 |
| exposure | 0.4732 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
