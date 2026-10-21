# EMA Hourly Continuation — AKT/USDT P89_200

**Symbol:** AKT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.8120 |
| net_win_rate | 0.4962 |
| gross_profit_factor | 0.9888 |
| gross_win_rate | 0.4962 |
| sharpe_ratio | -1.0904 |
| sortino_ratio | -0.2545 |
| max_drawdown | 0.2591 |
| cagr | -0.1115 |
| net_avg_win | 84.0721 |
| net_avg_loss | -101.9943 |
| avg_hold_time_bars | 14.6203 |
| exposure | 0.1768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
