# EMA Hourly Continuation — BTT/USDT P144_200

**Symbol:** BTT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 200 |
| net_profit_factor | 0.4468 |
| net_win_rate | 0.4450 |
| gross_profit_factor | 0.8285 |
| gross_win_rate | 0.4500 |
| sharpe_ratio | -3.6160 |
| sortino_ratio | -0.7430 |
| max_drawdown | 0.5816 |
| cagr | -0.2920 |
| net_avg_win | 52.6229 |
| net_avg_loss | -94.4330 |
| avg_hold_time_bars | 8.6650 |
| exposure | 0.0788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
