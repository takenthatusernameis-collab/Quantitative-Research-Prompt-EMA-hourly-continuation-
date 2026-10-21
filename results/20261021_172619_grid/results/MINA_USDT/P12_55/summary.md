# EMA Hourly Continuation — MINA/USDT P12_55

**Symbol:** MINA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.7944 |
| net_win_rate | 0.5116 |
| gross_profit_factor | 1.0409 |
| gross_win_rate | 0.5116 |
| sharpe_ratio | -1.8688 |
| sortino_ratio | -0.6827 |
| max_drawdown | 0.6268 |
| cagr | -0.2712 |
| net_avg_win | 63.7984 |
| net_avg_loss | -84.1090 |
| avg_hold_time_bars | 13.4977 |
| exposure | 0.3982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
