# EMA Hourly Continuation — ICP/USDT P34_89

**Symbol:** ICP/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.7116 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 0.9246 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -2.2567 |
| sortino_ratio | -0.6688 |
| max_drawdown | 0.5534 |
| cagr | -0.2639 |
| net_avg_win | 63.9704 |
| net_avg_loss | -83.0770 |
| avg_hold_time_bars | 10.6798 |
| exposure | 0.2092 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
