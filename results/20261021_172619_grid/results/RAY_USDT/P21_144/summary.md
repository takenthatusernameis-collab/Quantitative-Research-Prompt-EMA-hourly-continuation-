# EMA Hourly Continuation — RAY/USDT P21_144

**Symbol:** RAY/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.7895 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9325 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -1.4936 |
| sortino_ratio | -0.4202 |
| max_drawdown | 0.4570 |
| cagr | -0.1773 |
| net_avg_win | 77.2842 |
| net_avg_loss | -91.1042 |
| avg_hold_time_bars | 26.8154 |
| exposure | 0.4754 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
