# EMA Hourly Continuation — P2P/USDT P20_55

**Symbol:** P2P/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 885 |
| net_profit_factor | 0.3144 |
| net_win_rate | 0.3412 |
| gross_profit_factor | 0.4991 |
| gross_win_rate | 0.3435 |
| sharpe_ratio | -9.0364 |
| sortino_ratio | -3.7680 |
| max_drawdown | 0.9902 |
| cagr | -0.8415 |
| net_avg_win | 15.0328 |
| net_avg_loss | -24.7717 |
| avg_hold_time_bars | 6.4158 |
| exposure | 0.2581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
