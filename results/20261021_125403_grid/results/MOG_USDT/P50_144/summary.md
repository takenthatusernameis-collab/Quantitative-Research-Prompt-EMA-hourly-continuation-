# EMA Hourly Continuation — MOG/USDT P50_144

**Symbol:** MOG/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.7802 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 0.9198 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -1.4268 |
| sortino_ratio | -0.3789 |
| max_drawdown | 0.4198 |
| cagr | -0.1606 |
| net_avg_win | 76.2811 |
| net_avg_loss | -91.8108 |
| avg_hold_time_bars | 14.5094 |
| exposure | 0.2294 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
