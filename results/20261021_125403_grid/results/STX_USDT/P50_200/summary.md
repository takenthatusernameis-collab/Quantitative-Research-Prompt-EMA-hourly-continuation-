# EMA Hourly Continuation — STX/USDT P50_200

**Symbol:** STX/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.8013 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9745 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.0712 |
| sortino_ratio | -0.2593 |
| max_drawdown | 0.3128 |
| cagr | -0.1133 |
| net_avg_win | 73.2865 |
| net_avg_loss | -91.4624 |
| avg_hold_time_bars | 29.7188 |
| exposure | 0.3873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
