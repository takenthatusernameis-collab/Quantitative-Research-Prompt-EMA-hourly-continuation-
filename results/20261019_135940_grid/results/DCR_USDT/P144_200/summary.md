# EMA Hourly Continuation — DCR/USDT P144_200

**Symbol:** DCR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.4200 |
| net_win_rate | 0.4230 |
| gross_profit_factor | 0.8210 |
| gross_win_rate | 0.4425 |
| sharpe_ratio | -5.3336 |
| sortino_ratio | -1.5352 |
| max_drawdown | 0.8445 |
| cagr | -0.5204 |
| net_avg_win | 35.3001 |
| net_avg_loss | -61.6095 |
| avg_hold_time_bars | 4.6650 |
| exposure | 0.0863 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
