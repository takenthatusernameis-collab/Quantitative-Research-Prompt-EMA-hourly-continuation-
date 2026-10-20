# EMA Hourly Continuation — CFG/USDT P144_200

**Symbol:** CFG/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.5254 |
| net_win_rate | 0.4678 |
| gross_profit_factor | 0.8541 |
| gross_win_rate | 0.4702 |
| sharpe_ratio | -3.6174 |
| sortino_ratio | -1.0416 |
| max_drawdown | 0.7214 |
| cagr | -0.3944 |
| net_avg_win | 40.4583 |
| net_avg_loss | -67.6785 |
| avg_hold_time_bars | 4.6038 |
| exposure | 0.0877 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
