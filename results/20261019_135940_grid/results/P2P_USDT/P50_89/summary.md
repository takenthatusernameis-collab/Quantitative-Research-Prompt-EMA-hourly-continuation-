# EMA Hourly Continuation — P2P/USDT P50_89

**Symbol:** P2P/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 625 |
| net_profit_factor | 0.3967 |
| net_win_rate | 0.3632 |
| gross_profit_factor | 0.6017 |
| gross_win_rate | 0.3664 |
| sharpe_ratio | -6.9077 |
| sortino_ratio | -2.4237 |
| max_drawdown | 0.9480 |
| cagr | -0.6916 |
| net_avg_win | 27.4527 |
| net_avg_loss | -39.4736 |
| avg_hold_time_bars | 4.9472 |
| exposure | 0.1405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
