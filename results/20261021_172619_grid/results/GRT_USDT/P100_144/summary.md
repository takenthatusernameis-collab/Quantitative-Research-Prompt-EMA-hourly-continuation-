# EMA Hourly Continuation — GRT/USDT P100_144

**Symbol:** GRT/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 185 |
| net_profit_factor | 0.7386 |
| net_win_rate | 0.5027 |
| gross_profit_factor | 1.0052 |
| gross_win_rate | 0.5027 |
| sharpe_ratio | -1.2784 |
| sortino_ratio | -0.2492 |
| max_drawdown | 0.2920 |
| cagr | -0.1082 |
| net_avg_win | 76.2230 |
| net_avg_loss | -104.3232 |
| avg_hold_time_bars | 7.2378 |
| exposure | 0.0606 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
