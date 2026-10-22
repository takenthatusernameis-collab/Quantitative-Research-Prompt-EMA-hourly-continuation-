# EMA Hourly Continuation — GMT/USDT P12_200

**Symbol:** GMT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 0.9341 |
| net_win_rate | 0.5248 |
| gross_profit_factor | 1.1000 |
| gross_win_rate | 0.5248 |
| sharpe_ratio | -0.2800 |
| sortino_ratio | -0.0627 |
| max_drawdown | 0.2303 |
| cagr | -0.0318 |
| net_avg_win | 87.1535 |
| net_avg_loss | -103.0336 |
| avg_hold_time_bars | 70.7893 |
| exposure | 0.7787 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
