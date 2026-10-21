# EMA Hourly Continuation — KAS/USDT P144_200

**Symbol:** KAS/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 166 |
| net_profit_factor | 0.6492 |
| net_win_rate | 0.4699 |
| gross_profit_factor | 0.8704 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -1.6517 |
| sortino_ratio | -0.3038 |
| max_drawdown | 0.3205 |
| cagr | -0.1297 |
| net_avg_win | 69.8750 |
| net_avg_loss | -95.4083 |
| avg_hold_time_bars | 7.6867 |
| exposure | 0.0580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
