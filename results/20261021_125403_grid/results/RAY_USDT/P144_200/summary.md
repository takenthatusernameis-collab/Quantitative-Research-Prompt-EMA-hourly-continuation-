# EMA Hourly Continuation — RAY/USDT P144_200

**Symbol:** RAY/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 186 |
| net_profit_factor | 0.6946 |
| net_win_rate | 0.4785 |
| gross_profit_factor | 0.9088 |
| gross_win_rate | 0.4785 |
| sharpe_ratio | -1.5557 |
| sortino_ratio | -0.3022 |
| max_drawdown | 0.3019 |
| cagr | -0.1298 |
| net_avg_win | 75.3176 |
| net_avg_loss | -99.4833 |
| avg_hold_time_bars | 7.8495 |
| exposure | 0.0664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
