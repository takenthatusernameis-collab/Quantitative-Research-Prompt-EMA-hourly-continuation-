# EMA Hourly Continuation — ID/USDT P12_100

**Symbol:** ID/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 586 |
| net_profit_factor | 0.6696 |
| net_win_rate | 0.4881 |
| gross_profit_factor | 0.9705 |
| gross_win_rate | 0.4949 |
| sharpe_ratio | -2.8253 |
| sortino_ratio | -0.9623 |
| max_drawdown | 0.7000 |
| cagr | -0.3672 |
| net_avg_win | 48.5258 |
| net_avg_loss | -69.0859 |
| avg_hold_time_bars | 21.9522 |
| exposure | 0.5822 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
