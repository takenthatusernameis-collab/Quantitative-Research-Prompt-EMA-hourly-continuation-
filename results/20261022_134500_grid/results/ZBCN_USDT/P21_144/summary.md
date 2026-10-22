# EMA Hourly Continuation — ZBCN/USDT P21_144

**Symbol:** ZBCN/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.7767 |
| net_win_rate | 0.5123 |
| gross_profit_factor | 1.0684 |
| gross_win_rate | 0.5154 |
| sharpe_ratio | -2.0922 |
| sortino_ratio | -0.7612 |
| max_drawdown | 0.6513 |
| cagr | -0.3040 |
| net_avg_win | 61.7500 |
| net_avg_loss | -83.5132 |
| avg_hold_time_bars | 15.7215 |
| exposure | 0.4728 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
