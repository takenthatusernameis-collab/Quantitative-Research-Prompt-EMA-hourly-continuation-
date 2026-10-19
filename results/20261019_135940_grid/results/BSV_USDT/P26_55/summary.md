# EMA Hourly Continuation — BSV/USDT P26_55

**Symbol:** BSV/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1010 |
| net_profit_factor | 0.3400 |
| net_win_rate | 0.4099 |
| gross_profit_factor | 0.7422 |
| gross_win_rate | 0.4356 |
| sharpe_ratio | -9.9370 |
| sortino_ratio | -4.4935 |
| max_drawdown | 0.9965 |
| cagr | -0.8932 |
| net_avg_win | 12.3990 |
| net_avg_loss | -25.3303 |
| avg_hold_time_bars | 4.3980 |
| exposure | 0.2019 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
