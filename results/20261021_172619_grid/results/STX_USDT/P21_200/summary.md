# EMA Hourly Continuation — STX/USDT P21_200

**Symbol:** STX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.8644 |
| net_win_rate | 0.5055 |
| gross_profit_factor | 1.0187 |
| gross_win_rate | 0.5055 |
| sharpe_ratio | -0.6978 |
| sortino_ratio | -0.1642 |
| max_drawdown | 0.2500 |
| cagr | -0.0749 |
| net_avg_win | 82.9815 |
| net_avg_loss | -98.1457 |
| avg_hold_time_bars | 53.2472 |
| exposure | 0.6530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
